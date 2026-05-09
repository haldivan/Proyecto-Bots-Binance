import time
from bot.bot_logic import run_bot

def main():
    print("🚀 Iniciando bot...")

    while True:
        try:
            run_bot()
        except Exception as e:
            print(f"❌ Error en ejecución: {e}")
        
        # Ajusta este tiempo según tu estrategia
        time.sleep(60)


if __name__ == "__main__":
    main()