from venv import logger
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle,InputTextMessageContent

from telegram.ext import CallbackContext
import logging
from game1 import start_game1
from game2 import start_game2

print("handlers.py has been imported")

async def start(update: Update, context: CallbackContext) -> None:
    #button_handler(update, context)
    keyboard = [
        [InlineKeyboardButton("بازی با دوستان", switch_inline_query="")],
        [InlineKeyboardButton("درباره ما", callback_data='about_us')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('سلام! به ربات خوش آمدید.', reply_markup=reply_markup)

async def callback_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    callback_data = query.data

    # بررسی اینکه آیا دکمه اینلاین است یا دایرکت
    if callback_data.startswith("inline_"):
        # بررسی بازی‌ها از callback_data
        if callback_data.startswith("inline_game1_start"):     
            
            await start_game1(update, context)
        elif callback_data == "inline_game2_start":
            await start_game2(update, context)
        else:
            # سایر دکمه‌های اینلاین را پردازش کن
            pass


async def mention_handler(update: Update, context: CallbackContext):
    query = update.inline_query.query
    keyboard = [ [InlineKeyboardButton("شروع بازی", callback_data="inline_game1_start")], 
                [InlineKeyboardButton("آموزش بازی", callback_data="inline_game")] ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    results = [
        InlineQueryResultArticle(
            id='game',
            title= "شروع بازی",
            input_message_content=InputTextMessageContent("میخوای بازی رو شروع کنی؟ بزن روم"),
            reply_markup=reply_markup
        )
    ]
    await update.inline_query.answer(results)



