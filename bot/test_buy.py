import time
from bot.connection_demo import client

# ==========================================
# CONFIGURACIÓN DE LA PRUEBA
# ==========================================
SIMBOLO = 'AMDUSDT'
MONTO_USDT = 5.1       # Tu margen solicitado
APALANCAMIENTO = 3
TP_PORCENTAJE = 0.015  # 1.5%
SL_PORCENTAJE = 0.0075 # 0.75%

def forzar_compra_xrp():
    try:
        print(f"🚀 Iniciando orden de prueba forzada para {SIMBOLO}...")

        # 1. Configuración de Cuenta con Protección contra error -4046
        try:
            client.futures_change_margin_type(symbol=SIMBOLO, marginType='ISOLATED')
            print(f"✅ Modo AISLADO configurado.")
        except Exception as e:
            # Si el error dice que no hace falta cambiarlo, simplemente seguimos
            if "No need to change margin type" in str(e):
                print(f"ℹ️ El margen ya estaba en AISLADO. Continuando...")
            else:
                print(f"⚠️ Nota en Margen: {e}")

        try:
            client.futures_change_leverage(symbol=SIMBOLO, leverage=APALANCAMIENTO)
            print(f"✅ Apalancamiento a {APALANCAMIENTO}x.")
        except Exception as e:
            print(f"⚠️ Nota en Apalancamiento: {e}")    
        
        # 2. Obtener precio actual para calcular niveles
        ticker = client.futures_symbol_ticker(symbol=SIMBOLO)
        precio_actual = float(ticker['price'])
        
        # 3. Cálculos de Posición
        valor_nocional = MONTO_USDT * APALANCAMIENTO
        cantidad = round(valor_nocional / precio_actual, 1)
        
        tp_precio = round(precio_actual * (1 + TP_PORCENTAJE), 4)
        sl_precio = round(precio_actual * (1 - SL_PORCENTAJE), 4)

        print(f"📊 Detalles del Plan:")
        print(f"   - Precio Entrada: {precio_actual}")
        print(f"   - Cantidad: {cantidad} XRP")
        print(f"   - Take Profit: {tp_precio}")
        print(f"   - Stop Loss: {sl_precio}")

        # 4. EJECUCIÓN: Orden de Compra Market
        print(f"\n🔔 Enviando orden MARKET BUY...")
        orden_entrada = client.futures_create_order(
            symbol=SIMBOLO,
            side='BUY',
            type='MARKET',
            quantity=cantidad
        )
        print(f"✅ Posición abierta. ID: {orden_entrada['orderId']}")

        # 5. EJECUCIÓN: Órdenes de Salida (Oco-like)
        # Take Profit
        client.futures_create_order(
            symbol=SIMBOLO,
            side='SELL',
            type='TAKE_PROFIT_MARKET',
            stopPrice=tp_precio,
            closePosition=True
        )
        print(f"🎯 Orden Take Profit colocada.")

        # Stop Loss
        client.futures_create_order(
            symbol=SIMBOLO,
            side='SELL',
            type='STOP_MARKET',
            stopPrice=sl_precio,
            closePosition=True
        )
        print(f"🛡️ Orden Stop Loss colocada.")
        
        print(f"\n✨ ¡Prueba completada! Revisa tu panel en demo.binance.com")

    except Exception as e:
        print(f"❌ Error en la prueba: {e}")

if __name__ == "__main__":
    forzar_compra_xrp()