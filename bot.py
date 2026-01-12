from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = "TOKEN_BURAYA"

async def gunceladres(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("TSjQYavgJBGPr8iV3zH7qo1bx927qKVMwA")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("gunceladres", gunceladres))
    print("Bot aktif...")
    app.run_polling()

if __name__ == "__main__":
    main()
