# bot.py
import re
import os
import logging
import requests
from telegram import Update, MessageEntity
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = '5148319110:AAGe4XFc8akli8Hbr2r3LF0QZPyc-WZ3Pto'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_mesg = "Hi"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_mesg)

async def HandleMessage(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mesg = update.message.text
    print(mesg)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=mesg)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, HandleMessage))
    application.run_polling()

if __name__ == '__main__':
    main()