from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os
from flask import Flask, request
import telegram

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")

bot = telegram.Bot(token=TOKEN)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id

    # Simulação de pagamento aprovado
    bot.send_message(chat_id=chat_id, text="✅ Pagamento confirmado! Bem-vindo ao VIP!")
    bot.send_message(chat_id=chat_id, text=f"👉 Acesse o canal VIP: {CHANNEL_LINK}")

    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
