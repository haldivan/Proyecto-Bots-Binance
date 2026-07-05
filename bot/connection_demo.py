import os
import requests # Usaremos esto para ver la respuesta real del servidor
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('BINANCE_API_KEY_DEMO') 
api_secret = os.getenv('BINANCE_SECRET_KEY_DEMO')

# 1. VALIDACIÓN DE LLAVES: ¿VS Code realmente las está leyendo?
if not api_key or not api_secret:
    print("❌ ERROR CRÍTICO: No se detectan las llaves en el archivo .env")
    exit()

print(f"🕵️ Iniciando auditoría de conexión...")
print(f"🔑 Llave detectada: {api_key[:5]}...")

# 2. CONFIGURACIÓN DEL CLIENTE
client = Client(api_key, api_secret)
# Probamos con la URL base sin el /fapi al final, para que la librería lo gestione
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

try:
    # 3. PRUEBA DE PING (Sin firma)
    print("📡 Probando latencia con el servidor Demo...")
    server_time = client.futures_time()
    
    if server_time is None:
        print("❌ El servidor respondió 'None'. La URL 'https://demo-fapi.binance.com/fapi' podría estar bloqueada o ser incorrecta.")
    else:
        print(f"✅ Comunicación básica establecida. Hora: {server_time['serverTime']}")

        # 4. PRUEBA DE BALANCE (Con firma)
        print("🔑 Probando acceso a balances privados...")
        balances = client.futures_account_balance()
        
        if balances:
            usdt = next((item for item in balances if item["asset"] == "USDT"), None)
            if usdt:
                print(f"💰 ¡CONEXIÓN EXITOSA! Saldo Demo: {usdt['balance']} USDT")
            else:
                print("⚠️ Conectado, pero no se encontró la moneda USDT.")
        else:
            print("❌ El balance devolvió vacío. Revisa los permisos de la API Key en la web.")

except Exception as e:
    print(f"💥 FALLO DE PROTOCOLO: {e}")
    print("\n💡 Sugerencia técnica:")
    print("Si el error persiste, intenta cambiar la línea 18 a:")
    print("client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'")