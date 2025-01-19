<<<<<<< Updated upstream
import nest_asyncio # type: ignore
nest_asyncio.apply()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup # type: ignore
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes,InlineQueryHandler
from game1 import start_game1
from game2 import start_game2
from decorators import button_handler
from handlers import mention_handler, callback_handler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('سلام! به ربات خوش آمدید.')

async def main() -> None:
    # توکن ربات خود را اینجا قرار دهید
    TOKEN = "7847166209:AAFfQLo46-rMVJxfuL9MxXNM-QzP3nKUn5g"

    # مقداردهی اولیه Application
    application = Application.builder().token(TOKEN).build()

    # اضافه کردن handler برای دستور /start
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("game1", start_game1))
    application.add_handler(CommandHandler("game2", start_game2))
    application.add_handler(CallbackQueryHandler(callback_handler))
    application.add_handler(InlineQueryHandler(mention_handler))
    # شروع ربات
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
=======
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# توکن بات خود را اینجا قرار دهید
TOKEN = '7847166209:AAFfQLo46-rMVJxfuL9MxXNM-QzP3nKUn5g'

# تابع برای پاسخ به دستور /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! به بات تلگرامی خوش آمدید.')

# تابع برای پاسخ به پیام‌های متنی
def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    update.message.reply_text(f'شما گفتید: {user_message}')

def main() -> None:
    # ایجاد یک نمونه از Updater و ارسال توکن
    updater = Updater(TOKEN)

    # دریافت dispatcher برای ثبت handlerها
    dispatcher = updater.dispatcher

    # ثبت handler برای دستور /start
    dispatcher.add_handler(CommandHandler("start", start))

    # ثبت handler برای پیام‌های متنی
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # شروع بات
    updater.start_polling()

    # اجرای بات تا زمانی که Ctrl+C زده شود
    updater.idle()

if __name__ == '__main__':
    main()
>>>>>>> Stashed changes
