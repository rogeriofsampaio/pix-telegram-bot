from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask
import os
import threading

# Flask para manter vivo no Render
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot está rodando!"

# Variáveis ambiente
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_LINK = os.environ.get("CHANNEL_LINK")

# Comando start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Olá! Para acessar o canal VIP clique: {CHANNEL_LINK}")

# Função para rodar o bot
def run_telegram_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# Executar em thread separada
threading.Thread(target=run_telegram_bot).start()

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=10000)
