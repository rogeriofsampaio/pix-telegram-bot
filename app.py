from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import os
import threading

# Flask app apenas para manter o Render vivo
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot rodando!"

# Variáveis de ambiente
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_LINK = os.environ.get("CHANNEL_LINK")

# Handler do comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Olá! Entre no canal VIP: {CHANNEL_LINK}")

# Inicializar o bot com asyncio rodando em paralelo ao Flask
def run_telegram_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# Dispara o bot em outra thread para não bloquear o Flask
threading.Thread(target=run_telegram_bot).start()

if __name__ == "__main__":
    flask_app.ru_
