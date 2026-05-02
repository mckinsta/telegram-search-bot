from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT2_USERNAME

def start(update, context):
    update.message.reply_text("👋 Send movie name bhau!")

def search(update, context):
    query = update.message.text.lower().strip()

    # simple fake "search result"
    movie_name = query.replace(" ", "_")

    link = f"https://t.me/{BOT2_USERNAME}?start={movie_name}"

    keyboard = [
        [InlineKeyboardButton("🎬 Get Movie", url=link)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        f"🔍 Found: {query}",
        reply_markup=reply_markup
    )
