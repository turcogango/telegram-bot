import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# TOKEN'ı doğrudan kod içine yazabiliriz, ama Railway için ortam değişkeni kullanacağız
# Eğer tokenı kodda kullanmak istersen aşağıdaki satırı uncomment yap:
# TOKEN = "8089178738:AAH4o72dviLlAzNUIUsfEbOcwUewDDSW1iU"

# Railway’de Shared Variable olarak eklediysen:
TOKEN = os.getenv("TOKEN")

async def gunceladres(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("TSjQYavgJBGPr8iV3zH7qo1bx927qKVMwA")

def main():
    if not TOKEN:
        print("ERROR: Bot token is missing. Make sure the TOKEN variable is set!")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("gunceladres", gunceladres))
    print("Bot aktif...")
    app.run_polling()

if __name__ == "__main__":
    main()
