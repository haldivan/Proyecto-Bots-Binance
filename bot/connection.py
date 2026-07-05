import os
from binance.client import Client
from dotenv import load_dotenv

# Forzar sincronización de tiempo con los servidores de Binance
import time

# Cargar las variables del archivo .env
load_dotenv()

api_key=os.getenv('BINANCE_API_KEY')
api_secret=os.getenv('BINANCE_SECRET_KEY')

# Inicializar el cliente
client = Client(api_key, api_secret)

tiempo_servidor = client.get_server_time()
tiempo_local = int(time.time() * 1000)
client.timestamp_offset = tiempo_servidor['serverTime'] - tiempo_local  


def sincronizar_hora():
    try:
        tiempo_servidor = client.get_server_time()
        tiempo_local = int(time.time() * 1000)

        client.timestamp_offset = (tiempo_servidor['serverTime'] - tiempo_local)
        return True

    except Exception as e:
        print(f"⚠️ Error sincronizando hora: {e}")
        return False

try:
    # Obtener información de la cuenta
    account = client.get_account()

    # Filtrar solo las monedas que tienen saldo (para no ver una lista gigante)
    balances = [b for b in account['balances'] if float(b['free']) > 0]
    
    print("✅ Conexión exitosa. Tus saldos actuales:")
    for b in balances:
        print(f"Moneda: {b['asset']} | Libre: {b['free']}")

except Exception as e:
    print(f"❌ Error al conectar: {e}")