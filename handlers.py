from telegram import Update
from telegram.ext import CallbackContext
from keyboards import start_game_keyboard
from game1 import start_game1
from game2 import start_game2

print("handlers.py has been imported")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('برای شروع بازی دکمه زیر را فشار دهید:', reply_markup=start_game_keyboard())

async def callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    callback_data = query.data

    # بررسی اینکه آیا دکمه اینلاین است یا دایرکت
    if callback_data.startswith("inline_"):
        # بررسی بازی‌ها از callback_data
        if callback_data == "inline_game1_start":
            await start_game1(update, context)
        elif callback_data == "inline_game2_start":
            await start_game2(update, context)
        else:
            # سایر دکمه‌های اینلاین را پردازش کن
            await handle_inline_buttons(update, context)
    
    elif callback_data.startswith("direct_"):
        # پردازش دکمه‌های دایرکت
        await handle_direct_buttons(update, context)

async def handle_inline_buttons(update: Update, context: CallbackContext) -> None:
    # پردازش سایر دکمه‌های اینلاین
    await update.callback_query.answer("دکمه اینلاین دیگر")

async def handle_direct_buttons(update: Update, context: CallbackContext) -> None:
    # پردازش دکمه‌های دایرکت
    await update.callback_query.answer("دکمه دایرکت دیگر")
