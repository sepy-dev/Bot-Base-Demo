from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import random
from datetime import datetime, timedelta
from decorators import check_membership_and_rules


funny_texts = [
    "چرا مرغ از جاده رد شد؟ چون می‌خواست به آن طرف برسد!",
    "چه چیزی سبز است و می‌پرد؟ یک قورباغه‌ی عصبانی!",
    "چرا کامپیوتر سردش شد؟ چون ویندوزش باز بود!",
    "چه چیزی قرمز است و دور خانه می‌چرخد؟ یک آجر خون‌آشام!",
    "چرا کتاب‌ها به مهمانی رفتند؟ چون دعوت شده بودند!"
]

# لیست بازیکنان و متن‌های استفاده شده



@check_membership_and_rules(keygame="inline_game1_start")
async def start_game1(update: Update, context: CallbackContext, keygame: str, data: dict) -> None:
    # Reset game state
    data["used_texts"] = []
    data["current_player_index"] = 0
    data["last_activity_time"] = datetime.now()

    await update.message.reply_text('بازی 1 شروع شد!')

    # شروع بازی با اولین بازیکن
    await next_turn(update, context, data)

async def next_turn(update: Update, context: CallbackContext, data: dict) -> None:
    # بررسی زمان عدم فعالیت
    if data["last_activity_time"] and datetime.now() - data["last_activity_time"] > timedelta(minutes=15):
        await end_game(update, context, data)
        return

    # انتخاب بازیکن فعلی
    current_player = data["players"][data["current_player_index"]]
    data["last_activity_time"] = datetime.now()

    # انتخاب یک متن تصادفی از دیتابیس که قبلاً استفاده نشده باشد
    available_texts = [text for text in funny_texts if text not in data["used_texts"]]
    if not available_texts:
        # اگر همه متن‌ها استفاده شده‌اند، لیست را ریست می‌کنیم
        data["used_texts"] = []
        available_texts = funny_texts

    selected_text = random.choice(available_texts)
    data["used_texts"].append(selected_text)

    # ارسال متن به بازیکن فعلی
    await update.message.reply_text(
        f"نوبت {current_player}:\n{selected_text}",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("واکنشم رو نشون دادم", callback_data=f'{keygame}_reacted')]
        ])
    )

async def handle_reaction(update: Update, context: CallbackContext, keygame: str, data: dict) -> None:
    # بررسی اینکه آیا بازیکن فعلی واکنش نشان داده است
    query = update.callback_query
    user_id = query.from_user.id
    current_player = data["players"][data["current_player_index"]]

    if query.data == f'{keygame}_reacted':
        # حرکت به بازیکن بعدی
        data["current_player_index"] = (data["current_player_index"] + 1) % len(data["players"])
        await next_turn(update, context, data)

async def end_game(update: Update, context: CallbackContext, data: dict) -> None:
    # پاک کردن داده‌های بازی
    data["players"] = []
    data["used_texts"] = []
    data["current_player_index"] = 0
    data["last_activity_time"] = None

    await update.message.reply_text('بازی متوقف شد. می‌توانید بازی را از اول شروع کنید.')