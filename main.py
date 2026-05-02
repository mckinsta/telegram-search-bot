from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN

async def start(update, context):
    await update.message.reply_text("👋 Bot started bhau!")

async def search(update, context):
    query = update.message.text
    await update.message.reply_text(f"Searching: {query}")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

app.run_polling()
