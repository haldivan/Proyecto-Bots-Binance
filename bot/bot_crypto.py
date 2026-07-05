import pandas as pd
import sys
import datetime
import time # Asegúrate de importar time

# Estadísticas
import os
import csv
from pathlib import Path

# from bot.connection_demo import client
from connection import client   
from connection import sincronizar_hora



# ==========================================
# 1. PARÁMETROS GLOBALES
# ==========================================
# Eliminada POLUSDT
LISTA_CRIPTOS = ['SOLUSDT', 'XRPUSDT', 'ADAUSDT', 'DOTUSDT', 'TRXUSDT', 
                 'NEARUSDT', 'UNIUSDT', 'AVAXUSDT', 'BNBUSDT']

# LISTA_CRIPTOS = ['BNBUSDT', 'SOLUSDT', 'XRPUSDT', 'TRXUSDT', 'AVAXUSDT', 
#                 'ADAUSDT', 'UNIUSDT', 'NEARUSDT', 'DOTUSDT']


TEMPORALIDAD = '15m'
CANTIDAD_VELAS = 200
APALANCAMIENTO = 3
MONTO_MARGEN_FIJO = 2.5

MAX_POSICIONES = 3 # <--- TU LÍMITE DE SEGURIDAD

# Variables globales para el estado
# POSICIONES_ACTIVAS = {}

# Estadisticas
BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_ESTADISTICAS = BASE_DIR / "datos" / "estadisticas.csv"
ARCHIVO_SENALES = BASE_DIR / "datos" / "senales_detectadas.csv"

# ARCHIVO_ESTADISTICAS = "estadisticas.csv"
# ARCHIVO_SENALES = "senales_detectadas.csv"

# ==========================================
# CONFIGURACIÓN DEL SCORE NORMALIZADO
# ==========================================
SCORE_MODELO = "NORMALIZADO_V1"

PESO_TENDENCIA = 0.40
PESO_MOMENTUM = 0.40
PESO_RSI = 0.20

ESCALA_TENDENCIA = 100
ESCALA_MOMENTUM = 200

VENTANA_MACD_STD = 50

# VERSION_BOT = "Fase1_MACD_BTC1H"
VERSION_BOT = "Fase1.1_MACD_BTC1H" #Cambios en SCORE 


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
                return p_prec, q_prec, t_size
    except Exception as e: 
        print(f"Error obteniendo precisiones de {simbolo}: {e}")
        return 3, 1, 0.001
    return 3, 1, 0.001

def configurar_cuenta():
    print("⚙️ Configurando margen y apalancamiento...")
    for simbolo in LISTA_CRIPTOS:
        try: client.futures_change_margin_type(symbol=simbolo, marginType='ISOLATED')
        except: pass
        try: client.futures_change_leverage(symbol=simbolo, leverage=APALANCAMIENTO)
        except: pass

def tiene_posicion_abierta(simbolo):
    try:
        # futures_account() es el endpoint más robusto y menos restrictivo
        cuenta = client.futures_account()

        for p in cuenta['positions']:
            # Convertimos a float para asegurar comparación numérica
            # Buscamos específicamente el símbolo solicitado
            if p['symbol'] == simbolo:
                cantidad = float(p['positionAmt'])
                # Retornamos True si la cantidad es distinta de 0
                return cantidad != 0

            # FILTRO CRÍTICO: Solo es abierta si la cantidad es diferente de 0
            # if cantidad != 0:
            #     print(f"DEBUG: {simbolo} tiene posición: {cantidad}")
            #     estados[simbolo] = True
            # else:
            #     estados[simbolo] = False

            # FILTRO: Guardamos True solo si la cantidad es != 0
            # es_abierta = (cantidad != 0)
            # estados[simbolo] = es_abierta
            
            # DEBUG: Imprimir esto nos dirá qué está viendo el bot
            # if simbolo == "SOLUSDT":
            #    print(f"DEBUG_API: {simbolo} | Amt: {cantidad} | Es_Abierta: {es_abierta}")


        # Creamos un diccionario: { 'SOLUSDT': True/False, ... }
        # return {p['symbol']: float(p['positionAmt']) != 0 for p in info_cuenta['positions']}
    
        # for pos in info_cuenta['positions']: # posiciones:
        #     if pos['symbol'] == simbolo:
        #        cantidad = float(pos['positionAmt'])

                # DEBUG: Esto imprimirá exactamente qué detecta para cada moneda
        #        print(f"DEBUG: {simbolo} | Amt: {cantidad}")

                # if float(pos['positionAmt']) != 0: return True
            
                # Si la cantidad es distinta de 0, tienes posición
        #        return cantidad != 0
        
        # Si no encontramos el símbolo, asumimos que no hay posición
        return False

    except Exception as e:
        print(f"❌ Error al consultar cuenta global: {e}")
        return True
    

# --- NUEVO: Filtro Maestro BTC ---
def es_btc_alcista():
    try:
        # velas = client.futures_historical_klines('BTCUSDT', TEMPORALIDAD, '1 day ago', limit=50)
        # Añadido
        velas = client.futures_historical_klines('BTCUSDT', '1h', '7 days ago',limit=100)
        df = pd.DataFrame(velas, columns=['OT', 'Open', 'High', 'Low', 'Close', 'Vol', 'CT', 'QV', 'NT', 'TB', 'TQ', 'I'])
        df['Close'] = df['Close'].astype(float)

        # return df['Close'].iloc[-1] > df['Close'].rolling(50).mean().iloc[-1]

        ema20 = df['Close'].ewm(span=20, adjust=False).mean().iloc[-1] #Añadido
        ema50 = df['Close'].ewm(span=50, adjust=False).mean().iloc[-1] #Añadido

        return ema20 > ema50

    
    # except: return False
    except Exception as e: #Añadido
        print(f"⚠️ Error filtro BTC: {e}") #Añadido
        return False                        #Añadido

# ==========================================
# 3. DATOS Y ESTRATEGIA
# ==========================================
def obtener_datos(simbolo):
    try:
        velas = client.futures_historical_klines(simbolo, TEMPORALIDAD, '3 days ago', limit=CANTIDAD_VELAS)
        if not velas: return None
        df = pd.DataFrame(velas, columns=['OT', 'Open', 'High', 'Low', 'Close', 'Vol', 'CT', 'QV', 'NT', 'TB', 'TQ', 'I'])
        df[['Close', 'High', 'Low']] = df[['Close', 'High', 'Low']].apply(pd.to_numeric)
        return df
    except Exception as e:
        print(f"{simbolo}: {e}")
        return None

def calcular_score(ema20, sma50, macd, signal, macd_std, rsi, debug=False):
    """
    Calcula un Score Normalizado (0-100)
    independiente del precio nominal del activo.
    """

    # ---------------------------------------
    # Distancia entre medias
    # ---------------------------------------

    distancia_medias = abs((ema20 - sma50) / sma50)
    distancia_medias = min(distancia_medias * ESCALA_TENDENCIA, 1)

    # ---------------------------------------
    # Momentum MACD
    # ---------------------------------------

    macd_std = max(macd_std, 1e-9)
    momentum = abs(macd - signal) / macd_std
    momentum = min(momentum * ESCALA_MOMENTUM, 1)

    # ---------------------------------------
    # RSI
    # ---------------------------------------

    if 45 < rsi < 60:
        rsi_score = 1
    elif 40 < rsi < 65:
        rsi_score = 0.5
    else:
        rsi_score = 0

    # ---------------------------------------

    score = (distancia_medias * PESO_TENDENCIA + momentum * PESO_MOMENTUM + rsi_score * PESO_RSI)

    if debug:
    #    print(f"Distancia={distancia_medias:.3f} " f"Momentum={momentum:.3f} " f"RSI={rsi_score:.3f}")
        print(f"[DEBUG SCORE] " f"Distancia={distancia_medias:.3f} " f"Momentum={momentum:.3f} " f"RSI={rsi_score:.3f}")

    return round(score * 100, 2)

def analizar_estrategia(df, simbolo, num, btc_ok):
    # 1. Validación básica de datos
    if df is None or len(df) < 50: # return "ESPERAR", 0
        # Esto te avisará por qué no estás viendo nada en pantalla
        print(f"⚠️ [{num}] {simbolo}: Datos insuficientes (Len: {len(df) if df is not None else 0})")
        return "ESPERAR", 0, 0

    # 2. Cálculos base
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    
    # Añadido
    # MACD
    ema12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema26 = df['Close'].ewm(span=26, adjust=False).mean()

    df['MACD'] = ema12 - ema26
    df['SIGNAL'] = df['MACD'].ewm(span=9, adjust=False).mean()


    # 3. Cálculo RSI con protección total
    delta = df['Close'].diff()
    ganancia = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    perdida = (-delta.where(delta < 0, 0)).rolling(window=14).mean()

    # Evitar división por cero
    perdida = perdida.replace(0, 0.000000001)

    # Asignar RSI y asegurar que no haya valores nulos
    df['RSI'] = 100 - (100 / (1 + (ganancia / perdida)))
    df['RSI'] = df['RSI'].fillna(50)

    #rsi = 100 - (100 / (1 + (delta.where(delta > 0, 0).rolling(14).mean() / -delta.where(delta < 0, 0).rolling(14).mean())))
    #ultimo = df.iloc[-1]; precio, rsi, sma, ema20 = ultimo['Close'], ultimo['RSI'], ultimo['SMA_50'], ultimo['EMA_20']

    # 4. Extraer valores con seguridad
    try:
        ultimo = df.iloc[-1]
        precio = float(ultimo['Close'])
        rsi_actual = float(ultimo['RSI'])
        ema20 = float(ultimo['EMA_20'])
        sma50 = float(ultimo['SMA_50'])

        # Añadido
        macd = float(ultimo['MACD'])
        signal = float(ultimo['SIGNAL'])

        macd_std = (df["MACD"].tail(VENTANA_MACD_STD).std())
        if pd.isna(macd_std):
            macd_std = 1e-9
        macd_std = max(macd_std, 1e-9)

        # Versión alineada (más legible)
        # print(f"[{num:02d}] {simbolo:<8} | P: {precio:.4f} | RSI: {rsi_actual:>6.2f} | EMA20: {ema20:>8.4f} | SMA50: {sma50:>8.4f}")
        # Añadido
        print(
            f"[{num:02d}] {simbolo:<8} | "
            f"P: {precio:.4f} | "
            f"RSI: {rsi_actual:>6.2f} | "
            f"EMA20: {ema20:>8.4f} | "
            f"SMA50: {sma50:>8.4f} | "
            f"MACD: {macd:>8.4f} | "
            f"SIG:{signal:.5f}"
        )

        # Filtro BTC
        # btc_ok = es_btc_alcista()
       
        if (btc_ok and ema20 > sma50 and precio > sma50 and 45 < rsi_actual < 60 and macd > signal):
        #    score = abs(ema20 - sma50) + abs(macd - signal)
            score = calcular_score(ema20, sma50, macd, signal, macd_std, rsi_actual)

            return "ORDEN_COMPRA_LONG", precio, score
        if (not btc_ok and ema20 < sma50 and precio < sma50 and 40 < rsi_actual < 55 and macd < signal):
        #    score = abs(ema20 - sma50) + abs(macd - signal)
            score = calcular_score(ema20, sma50, macd, signal, macd_std, rsi_actual)
            return "ORDEN_VENTA_SHORT", precio, score
        
    except Exception as e:
        print(f"❌ Error en cálculos de {simbolo}: {e}")
        return "ESPERAR", 0, 0
    
    # AÑADIDO
    # return "ESPERAR", precio
    return "ESPERAR", precio, 0 

# ==========================================
# 4. CÁLCULOS Y ÓRDENES (Corregido)
# ==========================================
def ejecutar_orden_completa(simbolo, decision, score):
    def snap(v, t): return round(round(v / t) * t, 8)
    for intento in range(3):
        try:
            # 1. Obtención de datos técnicos
            p_prec, q_prec, tick_size = obtener_precisiones(simbolo)
            lado_entrada = 'BUY' if "LONG" in decision else 'SELL'
            lado_salida = 'SELL' if lado_entrada == 'BUY' else 'BUY'
            
            ticker = client.futures_symbol_ticker(symbol=simbolo)
            precio_fresco = float(ticker['price'])
            cant = round(MONTO_MARGEN_FIJO * APALANCAMIENTO / precio_fresco, q_prec)
            
            # 2. Entrada (Market) - Sin positionSide para One-Way
            client.futures_create_order(symbol=simbolo, side=lado_entrada, type='MARKET', quantity=cant)
            time.sleep(0.5) # Respiro necesario para que Binance registre la posición

            # 3. Cálculo de TP y SL
            if lado_entrada == 'BUY':
                tp = snap(precio_fresco * 1.030, tick_size)
                sl = snap(precio_fresco * 0.985, tick_size)
            else:
                tp = snap(precio_fresco * 0.970, tick_size)
                sl = snap(precio_fresco * 1.015, tick_size)

            direccion = "LONG" if lado_entrada == "BUY" else "SHORT" # Estadísticas 

            # 4. Salida con TP y SL (One-Way Mode)
            # closePosition=True cierra toda la posición abierta automáticamente
            # print(f" ⚙️ DEBUG {simbolo} -> Enviando TP: {tp} | SL: {sl}")

            client.futures_create_order(
                symbol=simbolo, 
                side=lado_salida, 
                type='TAKE_PROFIT_MARKET', 
                # stopPrice=f"{tp:.{p_prec}f}",
                stopPrice=str(tp), # <--- CAMBIO CLAVE AQUI 
                closePosition=True, 
                workingType='CONTRACT_PRICE'
                )
            
            client.futures_create_order(
                symbol=simbolo, 
                side=lado_salida, 
                type='STOP_MARKET', 
                # stopPrice=f"{sl:.{p_prec}f}",
                stopPrice=str(sl), # <--- CAMBIO CLAVE AQUI 
                closePosition=True, 
                workingType='CONTRACT_PRICE'
                )
            
            registrar_operacion(simbolo, direccion, precio_fresco, tp, sl, score) # Estadísticas

            print(f"✅ {simbolo} operado correctamente (TP: {tp}, SL: {sl})")
            return # Salimos del bucle si todo salió bien
        
        except Exception as e:
            error_str = str(e)
            if "-1021" in error_str:
                print("⚠️ Desfase horario al enviar orden.")
                sincronizar_hora()
                time.sleep(1)
                continue
            elif '-1007' in error_str or '-4028' in error_str or '-2015' in error_str:
                print(f"⚠️ Error de red/timeout {error_str}. Reintentando ({intento+1}/3)...")
                time.sleep(5) # Pausa necesaria para evitar el bloqueo del -2015
                continue
            else: 
                print(f"❌ Error crítico en {simbolo}: {error_str}")
                break


# ==========================================
# 5. ESTADÍSTICAS
# ==========================================
def inicializar_estadisticas():
    ARCHIVO_ESTADISTICAS.parent.mkdir(parents=True, exist_ok=True)

    if not os.path.exists(ARCHIVO_ESTADISTICAS):

        with open(ARCHIVO_ESTADISTICAS,mode='w',newline='',encoding='utf-8'
        ) as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["fecha_hora", "simbolo", "direccion", "precio_entrada", "tp", "sl", "score", "version", "score_modelo"])

def registrar_operacion(simbolo, direccion, precio_entrada, tp, sl, score):
    
    with open(ARCHIVO_ESTADISTICAS, mode='a', newline='', encoding='utf-8'
    ) as archivo:

        writer = csv.writer(archivo)
        writer.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            simbolo,
            direccion,
            round(precio_entrada, 8),
            round(tp, 8),
            round(sl, 8),
            round(score, 8),
            VERSION_BOT,
            SCORE_MODELO
        ])

def inicializar_senales():
    if not os.path.exists(ARCHIVO_SENALES):
        with open(ARCHIVO_SENALES, mode='w', newline='', encoding='utf-8'
        ) as archivo:

            writer = csv.writer(archivo)
            writer.writerow(["fecha_hora", "simbolo", "direccion", "precio", "score", "motivo", "version", "score_modelo"])

def registrar_senal(simbolo, direccion, precio, score, motivo):
#    VERSION_BOT = "Fase1_MACD_BTC1H"

    with open(ARCHIVO_SENALES, mode='a', newline='', encoding='utf-8'
    ) as archivo:

        writer = csv.writer(archivo)
        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            simbolo,
            direccion,
            round(precio, 8),
            round(score, 8),
            motivo,
            VERSION_BOT,
            SCORE_MODELO
        ])

# ==========================================
# 6. BUCLE
# ==========================================
inicializar_estadisticas() # ESTADÍSTICAS
inicializar_senales()
configurar_cuenta()

def calcular_segundos_para_cierre():
    ahora = datetime.datetime.now()
    return (15 - (ahora.minute % 15)) * 60 - ahora.second

def contar_posiciones_abiertas():
    try:
        cuenta = client.futures_account()
        # Suma 1 por cada posición donde la cantidad no sea cero
        activas = sum(1 for p in cuenta['positions'] if float(p['positionAmt']) != 0)
        return activas
    except Exception as e:
        if "-1021" in str(e):
            print("⚠️ Error temporal de sincronización.")
            sincronizar_hora()

            try:
                cuenta = client.futures_account()
                activas = sum(1 for p in cuenta["positions"] if float(p["positionAmt"]) != 0)
                return activas

            except Exception as e2:
                print(f"❌ Error tras resincronizar: {e2}")
                return 99

            # return 0
    
        print(f"❌ Error al contar posiciones activas: {e}")
        return 99 # Retornamos un número alto para bloquear nuevas compras por seguridad en caso de error

def run_bot():
    if abs(PESO_TENDENCIA + PESO_MOMENTUM + PESO_RSI - 1) > 1e-9:
        raise ValueError("Los pesos del score deben sumar 1.")

    while True:
        print("\n--- Iniciando revisión de lista de criptos ---")

        # 1. El Reloj Maestro: Sincronización con las velas
        seg_espera = calcular_segundos_para_cierre()
        for t in range(seg_espera, 0, -1):
           sys.stdout.write(f"\r⏳ Siguiente revisión en: {t//60:02d}:{t%60:02d} "); 
           sys.stdout.flush()
           time.sleep(1)
        
        print("\n\n--- Ciclo de análisis iniciado ---")

        # 2. Control de Riesgo: Verificamos espacio antes de gastar recursos
        sincronizar_hora()
        activas = contar_posiciones_abiertas()
        
        print(f"📊 Posiciones activas actuales: {activas}/{MAX_POSICIONES}")

        if activas >= MAX_POSICIONES:
            # Si estamos llenos, el 'continue' nos manda de vuelta al inicio del While
            # para esperar la próxima vela de 15 minutos. No escaneamos el mercado.
            print("🛑 Límite de 3 operaciones alcanzado. Omitiendo escaneo hasta el próximo ciclo.")
            continue

        # Filtro maestro BTC (una sola consulta por ciclo)
        btc_ok = es_btc_alcista()
        print(f"🟢 BTC Alcista: {btc_ok}")
      
        # 3. El Barrido (Solo llegamos aquí si activas < 4)
        candidatas = [] # Añadido para score
        for i, simbolo in enumerate(LISTA_CRIPTOS, 1):
            # Consultamos la posición específicamente para este símbolo
            if not tiene_posicion_abierta(simbolo):
                # Diagnóstico: verificamos si obtener_datos responde
                df = obtener_datos(simbolo)
                if df is not None:
                    # Añadido para score        
                    # dec, p = analizar_estrategia(df, simbolo, i)
                    dec, p, score = analizar_estrategia(df, simbolo, i, btc_ok)

                    print(f"   -> {simbolo} decisión: {dec}")

                    # <--- EL ÚNICO AJUSTE: Buscar activamente LONG o SHORT --->
                    # if "LONG" in dec or "SHORT" in dec:
                    if dec in ("ORDEN_COMPRA_LONG", "ORDEN_VENTA_SHORT"):
                        # print(f"   -> {simbolo} ejecutando orden: {dec}")
                        # ejecutar_orden_completa(simbolo, dec, p)
                    
                        #mos el contador local y frenamos si nos llenamos
                        # activas += 1
                        # if activas >= MAX_POSICIONES:
                        #     print("🛑 Límite máximo alcanzado durante este barrido. Deteniendo búsqueda.")
                        #     break # Rompe el ciclo FOR de monedas

                        print(f"   -> {simbolo} almacenando candidata: {dec}")
                        candidatas.append({"simbolo": simbolo, "decision": dec, "precio": p, "score": score})

                else:
                    print(f" ❌ {simbolo} ERROR: obtener_datos devolvió None.")
                
            else:
                # Solo imprime si realmente tiene posición
                print(f" 🔹 {simbolo} tiene posición abierta, omitiendo.")

            time.sleep(1)
        
        if candidatas:
            candidatas.sort(key=lambda x: x["score"], reverse=True)
            espacios = MAX_POSICIONES - activas
            seleccionadas = candidatas[:espacios]

            descartadas = candidatas[espacios:]
            for c in descartadas:
                registrar_senal(c["simbolo"], c["decision"], c["precio"], c["score"], "RANKING_INFERIOR")

            print("\n🏆 Ranking oportunidades:")
            for c in seleccionadas:
                print(f"{c['simbolo']} | " f"{c['decision']} | " f"Score={c['score']:.2f}")
                registrar_senal(c['simbolo'], c['decision'], c['precio'], c['score'], "OPERADA")
                ejecutar_orden_completa(c['simbolo'], c['decision'], c['score'])

        print("--- Ciclo finalizado ---\n")

if __name__ == "__main__":
    run_bot()