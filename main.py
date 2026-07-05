import time
# from bot.bot_logic import run_bot

import subprocess
import sys

def main():
#   print("🚀 Iniciando bots...")
    print("🚀 Iniciando Bot Crypto...")
    crypto = subprocess.Popen([sys.executable, "-m", "bot.bot_logic.py"])

    print("🚀 Iniciando Bot TradFi...")
    tradfi = subprocess.Popen([sys.executable, "-m", "bot.bot_tradfi.py"])

    print(f"✅ Crypto PID: {crypto.pid}")
    print(f"✅ TradFi PID: {tradfi.pid}")


#    print("✅ Bots lanzados.")
    while True:
        if crypto.poll() is not None:
            print("❌ Bot Crypto detenido")

        if tradfi.poll() is not None:
            print("❌ Bot TradFi detenido")

#        try:
#            run_bot()
#        except Exception as e:
#            print(f"❌ Error en ejecución: {e}")
        
        # Ajusta este tiempo según tu estrategia
        time.sleep(60)


if __name__ == "__main__":
    main()