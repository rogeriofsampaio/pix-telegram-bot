from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask, request
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_LINK = os.environ.get("CHANNEL_LINK")

application = ApplicationBuilder().token(BOT_TOKEN).build()

# Comando de teste
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Olá! Acesse nosso canal VIP: {CHANNEL_LINK}")

application.add_handler(CommandHandler("start", start))

# Inicializa o bot em segundo plano
async def run_bot():
    await application.initialize()
    await application.start()
    await application.updater.
