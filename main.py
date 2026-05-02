from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN
from handlers import start, search

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

app.run_polling()
