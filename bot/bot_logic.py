import pandas as pd
import time
import sys
# from test_connection import client

from bot.connection import client

# ==========================================
# 1. PARÁMETROS GLOBALES
# ==========================================
LISTA_CRIPTOS = ['BNBUSDT', 'XRPUSDT', 'TRXUSDT', 'ADAUSDT', 'ETHUSDT', 'SOLUSDT', 'LINKUSDT', 'DOTUSDT', 'LTCUSDT', 'POLUSDT']
TEMPORALIDAD = '15m'
CANTIDAD_VELAS = 200
APALANCAMIENTO = 3
MONTO_MARGEN_FIJO = 1.8 

# ==========================================
# 2. FUNCIONES DE PRECISIÓN Y CUENTA
# ==========================================
def obtener_precisiones(simbolo):
    try:
        info = client.futures_exchange_info()
        for s in info['symbols']:
            if s['symbol'] == simbolo:
                t_size = float(s['filters'][0]['tickSize'])
                s_size = float(s['filters'][1]['stepSize'])
                p_prec = len(str(t_size).split('.')[-1].rstrip('0')) if '.' in str(t_size) else 0
                q_prec = len(str(s_size).split('.')[-1].rstrip('0')) if '.' in str(s_size) else 0
                return p_prec, q_prec
    except: return 3, 1
    return 3, 1

def configurar_cuenta():
    print("⚙️ Configurando margen y apalancamiento...")
    for simbolo in LISTA_CRIPTOS:
        try: client.futures_change_margin_type(symbol=simbolo, marginType='ISOLATED')
        except: pass
        try: client.futures_change_leverage(symbol=simbolo, leverage=APALANCAMIENTO)
        except: pass

def tiene_posicion_abierta(simbolo):
    try:
        posiciones = client.futures_position_information(symbol=simbolo)
        for pos in posiciones:
            if float(pos['positionAmt']) != 0: return True
        return False
    except Exception as e: 
        # Ahora el bot te avisará si fue un salto por error de red
        print(f"⚠️ Red inestable consultando {simbolo}. Saltando por seguridad. Error: {e}")
        return True

# ==========================================
# 3. DATOS Y ESTRATEGIA
# ==========================================
def obtener_datos(simbolo):
    try:
        velas = client.futures_historical_klines(simbolo, TEMPORALIDAD, '3 days ago', limit=CANTIDAD_VELAS)

        # Alerta si Binance devuelve una lista vacía de velas
        if not velas:
            print(f"⚠️ Binance Demo no devolvió velas para {simbolo}.")
            return None

        df = pd.DataFrame(velas, columns=['OT', 'Open', 'High', 'Low', 'Close', 'Vol', 'CT', 'QV', 'NT', 'TB', 'TQ', 'I'])
        df[['Close', 'High', 'Low']] = df[['Close', 'High', 'Low']].apply(pd.to_numeric)
        return df
    except Exception as e:
        print(f"❌ Error de red descargando velas para {simbolo}: {e}")
        return None

def analizar_estrategia(df, simbolo, num):

    # Alerta si los datos son insuficientes
    if df is None or len(df) < 50: 
        print(f"⚠️ [{num}] {simbolo}: Datos insuficientes o error de conexión. Saltando...")
        return "ESPERAR", 0
    
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    delta = df['Close'].diff()
    ganancia = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    perdida = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    df['RSI'] = 100 - (100 / (1 + (ganancia / perdida)))
    
    ultimo = df.iloc[-1]; precio, rsi, sma = ultimo['Close'], ultimo['RSI'], ultimo['SMA_50']
    print(f"[{num}] {simbolo} | P: {precio:.4f} | RSI: {rsi:.2f} | SMA: {sma:.4f}")

    if rsi < 35 and precio > sma: return "ORDEN_COMPRA_LONG", precio
    if rsi > 65 and precio < sma: return "ORDEN_VENTA_SHORT", precio
    return "ESPERAR", precio

# ==========================================
# 4. CÁLCULOS Y ÓRDENES
# ==========================================
def calcular_parametros_orden(simbolo, precio_actual, decision):
    p_prec, q_prec = obtener_precisiones(simbolo)
    valor_nocional = MONTO_MARGEN_FIJO * APALANCAMIENTO
    
    # --- AQUÍ SE USA q_prec CORRECTAMENTE ---
    cantidad = round(valor_nocional / precio_actual, q_prec)
    
    # Lógica unificada de TP/SL para evitar errores de nombres
    if "LONG" in decision:
        tp = round(precio_actual * 1.030, p_prec)
        sl = round(precio_actual * 0.985, p_prec)
    else: # SHORT
        tp = round(precio_actual * 0.970, p_prec)
        sl = round(precio_actual * 1.015, p_prec)
        
    return cantidad, tp, sl

def ejecutar_orden_completa(simbolo, decision, precio_vela):
    """
    Versión Definitiva: Sincronización en tiempo real, casteo de precisión 
    y parche CONTRACT_PRICE para evitar errores -2021 y -1111.
    """
    try:
        # 1. Obtener precisiones dinámicas
        p_prec, q_prec = obtener_precisiones(simbolo)
        
        # 2. Definir flujo de órdenes
        lado_entrada = 'BUY' if "LONG" in decision else 'SELL'
        lado_salida = 'SELL' if lado_entrada == 'BUY' else 'BUY'
        
        # 3. OBTENER PRECIO FRESCO (Anula la latencia de la vela)
        ticker = client.futures_symbol_ticker(symbol=simbolo)
        precio_fresco = float(ticker['price'])
        
        # 4. Calcular cantidad con precisión exacta
        valor_nocional = MONTO_MARGEN_FIJO * APALANCAMIENTO
        cant = round(valor_nocional / precio_fresco, q_prec)
        
        print(f"🚀 [ENTRADA] Enviando {lado_entrada} Market en {simbolo}...")
        
        # 5. EJECUTAR ENTRADA
        orden_entrada = client.futures_create_order(
            symbol=simbolo, 
            side=lado_entrada, 
            type='MARKET', 
            quantity=cant
        )
        
        # 6. CAPTURAR PRECIO REAL DE LLENADO
        precio_real = float(orden_entrada.get('avgPrice', 0))
        if precio_real == 0:
            precio_real = precio_fresco
            
        print(f"✅ Entrada ejecutada a precio REAL: {precio_real}")

        # 7. CÁLCULO DE NIVELES
        if lado_entrada == 'BUY': # LONG
            tp_num = round(precio_real * 1.030, p_prec)
            sl_num = round(precio_real * 0.985, p_prec)
        else: # SHORT
            tp_num = round(precio_real * 0.970, p_prec)
            sl_num = round(precio_real * 1.015, p_prec)

        # 8. CASTEO A STRING EXACTO (Bloquea desbordamiento de coma flotante)
        tp_str = f"{tp_num:.{p_prec}f}"
        sl_str = f"{sl_num:.{p_prec}f}"

        # 9. ENVIAR PROTECCIONES CON PARCHE DE PRECIO
        try:
            # TAKE PROFIT
            client.futures_create_order(
                symbol=simbolo, 
                side=lado_salida, 
                type='TAKE_PROFIT_MARKET', 
                stopPrice=tp_str, 
                closePosition=True,
                workingType='CONTRACT_PRICE' # <-- Obliga a Binance a usar el precio real
            )
            print(f"🎯 Take Profit fijado: {tp_str}")
            
            # STOP LOSS
            client.futures_create_order(
                symbol=simbolo, 
                side=lado_salida, 
                type='STOP_MARKET', 
                stopPrice=sl_str, 
                closePosition=True,
                workingType='CONTRACT_PRICE' # <-- Obliga a Binance a usar el precio real
            )
            print(f"🛡️ Stop Loss fijado: {sl_str}")
            
        except Exception as e_salida:
            print(f"⚠️ Error enviando protecciones: {e_salida}")
            if '-2021' in str(e_salida):
                print("❗ RIESGO: Deslizamiento masivo detectado. La posición quedó sin protección.")

    except Exception as e:
        print(f"❌ Error crítico general en {simbolo}: {e}")

# ==========================================
# 5. BUCLE
# ==========================================
configurar_cuenta()
def run_bot():
    print("Bot ejecutándose...")
    while True:
        for i, simbolo in enumerate(LISTA_CRIPTOS, start=1):
            if tiene_posicion_abierta(simbolo):
                continue
            df_datos = obtener_datos(simbolo)
            decision, precio_actual = analizar_estrategia(df_datos, simbolo, i)
            if decision != "ESPERAR":
                ejecutar_orden_completa(simbolo, decision, precio_actual)
            time.sleep(1)

        for t in range(900, 0, -1):
            sys.stdout.write(f"\r⏳ Siguiente revisión en: {t//60:02d}:{t%60:02d} "); sys.stdout.flush()
            time.sleep(1)