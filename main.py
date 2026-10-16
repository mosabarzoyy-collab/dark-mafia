import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

MENU = [
    ["👤 پروفایل", "💰 کسب درآمد"],
    ["⚔️ مبارزه", "🛒 فروشگاه"],
    ["🎒 کوله‌پشتی", "📜 مأموریت‌ها"],
    ["🏴 کلن‌ها", "👑 قلمرو"],
    ["🤝 اتحادها", "🏆 رتبه‌بندی"],
    ["🎁 پاداش روزانه", "⚙️ تنظیمات"],
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        MENU,
        resize_keyboard=True
    )
    await update.message.reply_text(
        "👑 DARK MAFIA 👑\n\n"
        "💰 سکه: 1000\n"
        "⭐ سطح: 1\n"
        "❤️ سلامتی: 100\n\n"
        "به دنیای دارک مافیا خوش اومدی!\n"
        "از منوی زیر یک گزینه انتخاب کن.",
        reply_markup=keyboard
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 DARK MAFIA\n"
        "برای نمایش منوی بازی دستور /start رو بفرست."
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    responses = {
        "👤 پروفایل": "👤 پروفایل بازیکن\n⭐ سطح: 1\n💰 سکه: 1000\n❤️ سلامتی: 100",
        "💰 کسب درآمد": "💰 بخش کسب درآمد\nاین بخش به‌زودی تکمیل می‌شه.",
        "⚔️ مبارزه": "⚔️ بخش مبارزه\nاین بخش به‌زودی تکمیل می‌شه.",
        "🛒 فروشگاه": "🛒 فروشگاه بازی\nاین بخش به‌زودی تکمیل می‌شه.",
        "🎒 کوله‌پشتی": "🎒 کوله‌پشتی شما خالیه.",
        "📜 مأموریت‌ها": "📜 مأموریت‌ها به‌زودی اضافه می‌شن.",
        "🏴 کلن‌ها": "🏴 بخش کلن‌ها به‌زودی اضافه می‌شه.",
        "👑 قلمرو": "👑 بخش قلمرو به‌زودی اضافه می‌شه.",
        "🤝 اتحادها": "🤝 بخش اتحادها به‌زودی اضافه می‌شه.",
        "🏆 رتبه‌بندی": "🏆 جدول رتبه‌بندی به‌زودی اضافه می‌شه.",
        "🎁 پاداش روزانه": "🎁 پاداش روزانه به‌زودی فعال می‌شه.",
        "⚙️ تنظیمات": "⚙️ تنظیمات بازی به‌زودی اضافه می‌شه.",
    }

    await update.message.reply_text(
        responses.get(text, "یکی از گزینه‌های منو رو انتخاب کن.")
    )

def main():
    if not TOKEN:
        raise RuntimeError(
            "متغیر TELEGRAM_BOT_TOKEN در تنظیمات سرور تنظیم نشده."
        )

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler)
    )

    app.run_polling()

if __name__ == "__main__":
    main()
