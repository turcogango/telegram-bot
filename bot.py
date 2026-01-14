import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# TOKEN ortam değişkeninden okunacak
TOKEN = os.getenv("TOKEN")

# /gunceladres komutu
async def gunceladres(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("TSjQYavgJBGPr8iV3zH7qo1bx927qKVMwA")

# /gandalf komutu (4 taç)
async def gandalf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑👑👑👑")

def main():
    if not TOKEN:
        raise RuntimeError("TOKEN environment variable bulunamadı!")

    # Bot uygulamasını oluştur
    app = Application.builder().token(TOKEN).build()

    # Komutları ekle
    app.add_handler(CommandHandler("gunceladres", gunceladres))
    app.add_handler(CommandHandler("gandalf", gandalf))

    print("Bot aktif...")
    app.run_polling()

if __name__ == "__main__":
    main()
