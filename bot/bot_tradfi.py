import pandas as pd
import time
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
# VERSION_BOT = "Fase1_MACD_QQQ1H"
# VERSION_BOT = "Fase1.1_MACD_QQQ1H (2026-06-30)"
VERSION_BOT = "Fase1.2_MACD_QQQ1H"

LISTA_TRADFI = ['NVDAUSDT', 'AMDUSDT', 'MSFTUSDT', 'AAPLUSDT']

TEMPORALIDAD = '1h'
CANTIDAD_VELAS = 200
APALANCAMIENTO = 1
MONTO_MARGEN_FIJO = 5

# Variables globales para el estado
POSICIONES_ACTIVAS = {}

# Estadisticas
BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO_ESTADISTICAS = BASE_DIR / "datos" / "estadisticas_tradfi.csv"
ARCHIVO_HEARTBEAT = BASE_DIR / "datos" / "heartbeat.txt"
MODO_OBSERVACION = True

# ==========================================
# CONFIGURACIÓN DEL SCORE
# ==========================================
SCORE_MODELO = "NORMALIZADO_V1" 

PESO_TENDENCIA = 0.40
PESO_MOMENTUM = 0.40
PESO_RSI = 0.20

ESCALA_TENDENCIA = 100
ESCALA_MOMENTUM = 200

VENTANA_MACD_STD = 50





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
        return 3,1,0.001
    return 3, 1, 0.001

def configurar_cuenta():
    print("⚙️ Configurando margen y apalancamiento...")
    for simbolo in LISTA_TRADFI:
        print(f"Configurando {simbolo}")
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
    

# --- NUEVO: Filtro Maestro QQQ ---
def es_qqq_alcista():
    try:
    #    velas = client.futures_historical_klines('QQQUSDT', '1h', '15 days ago', limit=200)
        velas = client.futures_klines(symbol="QQQUSDT", interval="1h", limit=200)
        df = pd.DataFrame(velas, columns=['OT','Open','High','Low','Close','Vol','CT','QV','NT','TB','TQ','I'])
        df['Close'] = df['Close'].astype(float)

        ema20 = df['Close'].ewm(span=20, adjust=False).mean().iloc[-1]
        ema50 = df['Close'].ewm(span=50, adjust=False).mean().iloc[-1]

        print(f"QQQ -> EMA20:{ema20:.2f} "
            f"| EMA50:{ema50:.2f}"
            f" | Alcista={ema20 > ema50}"
        )

        return ema20 > ema50, ema20, ema50

    except Exception as e:
        print(f"Error QQQ: {e}")
        return False, 0, 0


# ==========================================
# 3. DATOS Y ESTRATEGIA
# ==========================================
def obtener_datos(simbolo):
    try:
    #    velas = client.futures_historical_klines(simbolo, TEMPORALIDAD, '15 days ago', limit=CANTIDAD_VELAS)
        velas = client.futures_klines(symbol=simbolo, interval=TEMPORALIDAD, limit=CANTIDAD_VELAS)
        if not velas: return None
        df = pd.DataFrame(velas, columns=['OT', 'Open', 'High', 'Low', 'Close', 'Vol', 'CT', 'QV', 'NT', 'TB', 'TQ', 'I'])
        df[['Open', 'Close', 'High', 'Low']] = df[['Open', 'Close', 'High', 'Low']].apply(pd.to_numeric)
        return df
    except Exception as e:
        print(f"{simbolo}: {e}")
        return None

def calcular_score(ema20, sma50, macd, signal, macd_std, rsi, debug=False):

    # -------------------------
    # Distancia medias
    # -------------------------

    distancia_medias = abs((ema20 - sma50) / sma50)
    # tendencia = min(tendencia * 100, 1)
    distancia_medias = min(distancia_medias * ESCALA_TENDENCIA, 1)

    # -------------------------
    # Momentum
    # -------------------------

    # momentum = abs(macd - signal) / precio
    # macd_std = df["MACD"].tail(50).std()
    macd_std = max(macd_std, 1e-9)
    momentum = abs(macd - signal) / macd_std
    # momentum = min(momentum * 200, 1)
    momentum = min(momentum * ESCALA_MOMENTUM, 1)

    # -------------------------
    # RSI
    # -------------------------

    if 50 <= rsi <= 65:
        rsi_score = 1
    elif 45 <= rsi <= 70:
        rsi_score = 0.5
    else:
        rsi_score = 0

    score = (distancia_medias  * PESO_TENDENCIA + momentum * PESO_MOMENTUM + rsi_score * PESO_RSI)

    if debug:
        print(f"Distancia medias={distancia_medias:.3f} " f"Momentum={momentum:.3f} " f"RSI={rsi_score:.3f}")

    return round(score * 100, 2)

def analizar_estrategia(df, simbolo, num, qqq_ok):
    # 1. Validación básica de datos
    if df is None or len(df) < 50: # return "ESPERAR", 0
        # Esto te avisará por qué no estás viendo nada en pantalla
        print(f"⚠️ [{num}] {simbolo}: Datos insuficientes (Len: {len(df) if df is not None else 0})")
        return "ESPERAR", 0, 0, None

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

        # # =====================================================
        # # DEBUG TEMPORALIDAD
        # # Verificar qué vela devuelve Binance como última
        # # =====================================================
        # print("\n================ DEBUG VELAS ================")
        # print("\n" + "=" * 70)
        # print("DEBUG TEMPORALIDAD")
        # print("=" * 70)

        # print(f"Símbolo      : {simbolo}")
        # print(f"Hora sistema : {datetime.datetime.now()}")

        # print("\nPENÚLTIMA VELA")
        # print("Penúltima OT:", datetime.datetime.fromtimestamp(int(df.iloc[-2]["OT"]) / 1000))
        # print("Penúltima CT:", datetime.datetime.fromtimestamp(int(df.iloc[-2]["CT"]) / 1000))
        
        # print("\nÚLTIMA VELA")
        # print("Última OT   :", datetime.datetime.fromtimestamp(int(df.iloc[-1]["OT"]) / 1000))
        # print("Última CT   :", datetime.datetime.fromtimestamp(int(df.iloc[-1]["CT"]) / 1000))
        
        # Versión alineada (más legible)
        # print(f"[{num:02d}] {simbolo:<8} | P: {precio:.4f} | RSI: {rsi_actual:>6.2f} | EMA20: {ema20:>8.4f} | SMA50: {sma50:>8.4f}")
        # Añadido
        print(f"[{num:02d}] {simbolo:<8} | " f"P: {precio:.4f} | " f"RSI: {rsi_actual:>6.2f} | " f"EMA20: {ema20:>8.4f} | " f"SMA50: {sma50:>8.4f} | "
            f"MACD: {macd:>8.4f} | "
            f"SIG:{signal:.5f}"
        )

        # score = abs(ema20 - sma50) + abs(macd - signal)
        macd_std = df["MACD"].tail(VENTANA_MACD_STD).std()
        score = calcular_score(ema20, sma50, macd, signal, macd_std, rsi_actual)
        if (qqq_ok and ema20 > sma50 and precio > sma50 and 50 < rsi_actual < 65 and macd > signal):
            fecha_hora = datetime.datetime.fromtimestamp(int(df.iloc[-1]["OT"]) / 1000)
            return "ORDEN_COMPRA_LONG", precio, score, fecha_hora
        
        if (not qqq_ok and ema20 < sma50 and precio < sma50 and 35 < rsi_actual < 50 and macd < signal):
            fecha_hora = datetime.datetime.fromtimestamp(int(df.iloc[-1]["OT"]) / 1000)
            return "ORDEN_VENTA_SHORT", precio, score, fecha_hora

        # Aplicación del Filtro QQQ Maestro
        # if qqq_ok and ema20 > sma and precio > sma and 45 < rsi < 60: return "ORDEN_COMPRA_LONG", precio
        # if not qqq_ok and ema20 < sma and precio < sma and 40 < rsi < 55: return "ORDEN_VENTA_SHORT", precio
        
    except Exception as e:
        print(f"❌ Error en cálculos de {simbolo}: {e}")
        return "ESPERAR", 0, 0, None
    
    # AÑADIDO
    # return "ESPERAR", precio
    return "ESPERAR", precio, 0, None

def calcular_tp_sl(simbolo, decision, precio):
    _, _, tick_size = obtener_precisiones(simbolo)

    def snap(v, t):
        return round(round(v / t) * t, 8)

    if "LONG" in decision:
        tp = snap(precio * 1.040, tick_size)
        sl = snap(precio * 0.980, tick_size)
    else:
        tp = snap(precio * 0.960, tick_size)
        sl = snap(precio * 1.020, tick_size)

    return tp, sl

# ==========================================
# 4. CÁLCULOS Y ÓRDENES (Corregido)
# ==========================================
def ejecutar_orden_completa(simbolo, decision, precio_vela, score, qqq_ema20, qqq_ema50, fecha_hora):
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
                tp = snap(precio_fresco * 1.040, tick_size)
                sl = snap(precio_fresco * 0.980, tick_size)
            else:
                tp = snap(precio_fresco * 0.960, tick_size)
                sl = snap(precio_fresco * 1.020, tick_size)

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
            
            registrar_operacion(simbolo, direccion, precio_fresco, tp, sl, "REAL", score, qqq_ema20, qqq_ema50, fecha_hora) # Estadísticas

            print(f"✅ {simbolo} operado correctamente (TP: {tp}, SL: {sl})")
            return # Salimos del bucle si todo salió bien
        
        except Exception as e:
            error_str = str(e)
            if '-1007' in error_str or '-4028' in error_str or '-2015' in error_str:
                print(f"⚠️ Error de red/timeout {error_str}. Reintentando ({intento+1}/3)...")
                time.sleep(5) # Pausa necesaria para evitar el bloqueo del -2015
            else: 
                print(f"❌ Error crítico en {simbolo}: {error_str}")
                break


# ==========================================
# 5. ESTADÍSTICAS
# ==========================================
def actualizar_heartbeat():
    with open(ARCHIVO_HEARTBEAT, "w",encoding="utf-8"
    ) as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

def inicializar_estadisticas():
    if not os.path.exists(ARCHIVO_ESTADISTICAS):

        with open(ARCHIVO_ESTADISTICAS,mode='w',newline='',encoding='utf-8'
        ) as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["fecha_hora", "simbolo", "direccion", "precio_entrada", "tp", "sl", "version", "score_modelo", "modo", "score", 
                             "qqq_ema20", "qqq_ema50", "estado", "fecha_fin", "precio_cierre", "resultado", "vela_cierre","ultima_vela_revisada"])   

def registrar_operacion(simbolo, direccion, precio_entrada, tp, sl, modo, score, qqq_ema20, qqq_ema50, fecha_hora):
    with open(ARCHIVO_ESTADISTICAS, mode='a', newline='', encoding='utf-8'
    ) as archivo:

        writer = csv.writer(archivo)
        writer.writerow([fecha_hora.strftime("%Y-%m-%d %H:%M:%S"),
            simbolo,
            direccion,
            round(precio_entrada, 8),
            round(tp, 8),
            round(sl, 8),
            VERSION_BOT,
            SCORE_MODELO,
            modo,
            round(score, 8),
            round(qqq_ema20,4),
            round(qqq_ema50,4),
            "ABIERTA",
            "",
            "",
            "",
            "",    # vela_cierre
            ""     # ultima_vela_revisada
        ])

def actualizar_observaciones():
    if not os.path.exists(ARCHIVO_ESTADISTICAS):
        return

    try:
        df = pd.read_csv(ARCHIVO_ESTADISTICAS)
    except Exception as e:
        print(f"❌ Error leyendo estadísticas: {e}")
        return

    if "estado" not in df.columns:
        return

    cambios = 0

    for idx, fila in df.iterrows():
        if fila["estado"] != "ABIERTA":
            continue

        simbolo = fila["simbolo"]
        direccion = str(fila["direccion"])

        tp = float(fila["tp"])
        sl = float(fila["sl"])

        try:
            if (pd.notna(fila["ultima_vela_revisada"]) and str(fila["ultima_vela_revisada"]).strip() != ""):
                fecha_inicio = pd.to_datetime(fila["ultima_vela_revisada"])

            else:
                fecha_inicio = pd.to_datetime(fila["fecha_hora"])

            fecha_binance = fecha_inicio.strftime("%d %b %Y %H:%M:%S")
            velas = client.futures_historical_klines(simbolo, TEMPORALIDAD, fecha_binance, limit=500)

            cerrar = False
            resultado = ""
            precio_cierre = 0
            fecha_fin = None

            for vela in velas[1:]:
                high = float(vela[2])
                low = float(vela[3])

                fecha_vela = datetime.datetime.fromtimestamp(int(vela[0]) / 1000)

                # ==========================
                # LONG
                # ==========================

                if "LONG" in direccion:
                    toca_tp = high >= tp
                    toca_sl = low <= sl

                    # ambos en misma vela
                    if toca_tp and toca_sl:
                        resultado = "SL"
                        precio_cierre = sl

                    #   fecha_fin = fecha_vela
                        fecha_fin = fecha_vela + obtener_duracion_temporalidad()

                        cerrar = True
                        break

                    if toca_tp:
                        resultado = "TP"
                        precio_cierre = tp

                    #   fecha_fin = fecha_vela
                        fecha_fin = fecha_vela + obtener_duracion_temporalidad()
                        
                        cerrar = True
                        break

                    if toca_sl:

                        resultado = "SL"
                        precio_cierre = sl

                    #    fecha_fin = fecha_vela
                        fecha_fin = fecha_vela + obtener_duracion_temporalidad()

                        cerrar = True
                        break

                # ==========================
                # SHORT
                # ==========================

                else:
                    toca_tp = low <= tp
                    toca_sl = high >= sl

                    # ambos en misma vela
                    if toca_tp and toca_sl:
                        resultado = "SL"
                        precio_cierre = sl

                    #   fecha_fin = fecha_vela
                        fecha_fin = fecha_vela + obtener_duracion_temporalidad()

                        cerrar = True
                        break

                    if toca_tp:
                        resultado = "TP"
                        precio_cierre = tp

                    #   fecha_fin = fecha_vela
                        fecha_fin = fecha_vela + obtener_duracion_temporalidad()

                        cerrar = True
                        break

                    if toca_sl:
                        resultado = "SL"
                        precio_cierre = sl

                    #   fecha_fin = fecha_vela
                        fecha_fin = fecha_vela + obtener_duracion_temporalidad()

                        cerrar = True
                        break

            if cerrar:
                df.at[idx, "estado"] = resultado
                df.at[idx, "fecha_fin"] = (fecha_fin.strftime("%Y-%m-%d %H:%M:%S"))
                df.at[idx, "precio_cierre"] = (precio_cierre)
                df.at[idx, "resultado"] = (resultado)

                if "vela_cierre" in df.columns:
                    df.at[idx, "vela_cierre"] = (fecha_vela.strftime("%Y-%m-%d %H:%M:%S"))
                
                if "ultima_vela_revisada" in df.columns:
                    df.at[idx, "ultima_vela_revisada"] = (fecha_fin.strftime("%Y-%m-%d %H:%M:%S"))

                cambios += 1
                print(f"✅ {simbolo} " f"{resultado} " f"@ {precio_cierre} " f"({fecha_fin})")


            if (not cerrar and len(velas) > 1):
                ultima_fecha = datetime.datetime.fromtimestamp(int(velas[-1][0]) / 1000) + obtener_duracion_temporalidad()
                df.at[idx, "ultima_vela_revisada"] = ultima_fecha.strftime("%Y-%m-%d %H:%M:%S")

        except Exception as e:
            print(f"❌ Error revisando " f"{simbolo}: {e}")

    df.to_csv(ARCHIVO_ESTADISTICAS, index=False)
    if cambios > 0:
        print(f"\n📊 Observaciones actualizadas: " f"{cambios}")


def obtener_duracion_temporalidad():
    mapa = {
        "15m": datetime.timedelta(minutes=15),
        "30m": datetime.timedelta(minutes=30),
        "1h": datetime.timedelta(hours=1),
        "2h": datetime.timedelta(hours=2),
        "4h": datetime.timedelta(hours=4),
        "1d": datetime.timedelta(days=1),
    }

    return mapa.get(TEMPORALIDAD, datetime.timedelta(hours=1))

# ==========================================
# 6. BUCLE
# ==========================================
inicializar_estadisticas() # ESTADÍSTICAS
configurar_cuenta()

def calcular_segundos_para_cierre():
    ahora = datetime.datetime.now()
    siguiente_hora = (ahora.replace(minute=0, second=0, microsecond=0) + datetime.timedelta(hours=1))
    return int((siguiente_hora - ahora).total_seconds())
    # return (59 - (ahora.minute % 60)) * 60 - ahora.second

def contar_posiciones_abiertas():
    try:
        cuenta = client.futures_account()
        # Suma 1 por cada posición donde la cantidad no sea cero
        activas = sum(1 for p in cuenta['positions'] if float(p['positionAmt']) != 0)
        return activas
    except Exception as e:
        print(f"❌ Error al contar posiciones activas: {e}")
        return 99 # Retornamos un número alto para bloquear nuevas compras por seguridad en caso de error

# def contar_posiciones_abiertas_grupo(lista_simbolos):
#     try:
#         cuenta = client.futures_account()
#         activas = sum(1 for p in cuenta['positions'] if (p['symbol'] in lista_simbolos and float(p['positionAmt']) != 0))
#         return activas
#     except Exception as e:
#         print(f"Error conteo: {e}")
#         return 99

def contar_posiciones_abiertas_grupo(lista_simbolos):
    try:
        cuenta = client.futures_account()
        activas = sum(1 for p in cuenta['positions']
            if (p['symbol'] in lista_simbolos and float(p['positionAmt']) != 0)
        )
        return activas

    except Exception as e:
        if "-1021" in str(e):
            print("⚠️ Desfase horario detectado.")
            print("🔄 Re-sincronizando hora con Binance...")
            try:
                sincronizar_hora()
                cuenta = client.futures_account()
                activas = sum(1 for p in cuenta['positions']
                    if (p['symbol'] in lista_simbolos and float(p['positionAmt']) != 0)
                )
                print("✅ Hora sincronizada correctamente.")
                return activas

            except Exception as e2:
                print(f"❌ Error tras resincronizar: {e2}")
                return 99

        print(f"❌ Error conteo: {e}")
        return 99


def run_bot():
    MAX_POSICIONES = 2 # <--- TU LÍMITE DE SEGURIDAD

    while True:
        print("\n--- Iniciando revisión de lista de tradfi ---")

        # 1. El Reloj Maestro: Sincronización con las velas
        seg_espera = calcular_segundos_para_cierre()
        for t in range(seg_espera, 0, -1):
           sys.stdout.write(f"\r⏳ Siguiente revisión en: {t//60:02d}:{t%60:02d} "); 
           sys.stdout.flush()
           time.sleep(1)

        # print("\n\n--- Ciclo de análisis iniciado ---")
        actualizar_heartbeat()
        ahora = datetime.datetime.now()
        print(f"\n{'='*60}\n" f"❤️ Heartbeat: " f"🚀 --- Ciclo de análisis iniciado --- " f"{ahora.strftime('%Y-%m-%d %H:%M:%S')}\n" f"{'='*60}")
        
        try:
            sincronizar_hora()
        except Exception as e:
            print(f"⚠️ Error sincronizando hora: {e}")

        actualizar_observaciones()

        # 2. Control de Riesgo: Verificamos espacio antes de gastar recursos
        activas = contar_posiciones_abiertas_grupo(LISTA_TRADFI)
        print(f"📊 Posiciones activas actuales: {activas}/{MAX_POSICIONES}")

        if activas >= MAX_POSICIONES:
            # Si estamos llenos, el 'continue' nos manda de vuelta al inicio del While
            # para esperar la próxima vela de 15 minutos. No escaneamos el mercado.
            print("🛑 Límite de 2 operaciones alcanzado. Omitiendo escaneo hasta el próximo ciclo.")
            continue

        # 3. El Barrido (Solo llegamos aquí si activas < 4)
        candidatas = [] # Añadido para score

        qqq_ok, qqq_ema20, qqq_ema50 = es_qqq_alcista()
        # qqq_estado = "QQQ_ALCISTA" if qqq_ok else "QQQ_BAJISTA"

        for i, simbolo in enumerate(LISTA_TRADFI, 1):
            # Consultamos la posición específicamente para este símbolo
            if not tiene_posicion_abierta(simbolo):
                # Diagnóstico: verificamos si obtener_datos responde
                df = obtener_datos(simbolo)
                if df is not None:
                    # Añadido para score        
                    # dec, p = analizar_estrategia(df, simbolo, i)
                    dec, p, score, fecha_hora = analizar_estrategia(df, simbolo, i, qqq_ok)

                    print(f"   -> {simbolo} decisión: {dec}")

                    # <--- EL ÚNICO AJUSTE: Buscar activamente LONG o SHORT --->
                    if "LONG" in dec or "SHORT" in dec:

                        # print(f"   -> {simbolo} ejecutando orden: {dec}")
                        # ejecutar_orden_completa(simbolo, dec, p)
                    
                        # # Actualizamos el contador local y frenamos si nos llenamos
                        # activas += 1
                        # if activas >= MAX_POSICIONES:
                        #     print("🛑 Límite máximo alcanzado durante este barrido. Deteniendo búsqueda.")
                        #     break # Rompe el ciclo FOR de monedas

                        print(f"   -> {simbolo} almacenando candidata: {dec}")
                        candidatas.append({"simbolo": simbolo, "decision": dec, "precio": p, "score": score, "fecha_hora": fecha_hora})

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
            print("\n🏆 Ranking oportunidades:")
            
            for c in seleccionadas:
                print(f"{c['simbolo']} | " f"{c['decision']} | " f"Score={c['score']:.6f}")

                if MODO_OBSERVACION:
                    tp, sl = calcular_tp_sl(c['simbolo'], c['decision'], c['precio'])
                    print(f"👁️ OBSERVACIÓN -> " f"{c['simbolo']} " f"{c['decision']} " f"Score={c['score']:.6f} "f"TP={tp} " f"SL={sl}")
                    registrar_operacion(c['simbolo'], c['decision'], c['precio'], tp, sl, "OBSERVACION", c['score'], qqq_ema20, qqq_ema50, c["fecha_hora"])
                else:
                    ejecutar_orden_completa(c['simbolo'], c['decision'], c['precio'], c['score'],qqq_ema20, qqq_ema50, c["fecha_hora"])

        print("--- Ciclo finalizado ---\n")

if __name__ == "__main__":
    run_bot()