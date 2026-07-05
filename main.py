from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8800253065:AAHh_2HNTU4Jb4MyqZ2jwTcZxf0rUVCOE4E"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بيك في بوت VIP 👋")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("وصلت رسالتك، ولسه بنطور البوت 😎")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
