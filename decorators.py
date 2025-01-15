from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import httpx
from users import is_user_in_channels  # اضافه کردن تابع بررسی عضویت

players = []

def check_membership_and_rules(func):
    async def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
        user_id = update.effective_user.id
        try:
            # بررسی عضویت کاربر در کانال‌ها
            is_member = await is_user_in_channels(user_id, context)

            # بررسی قوانین
            rules_ok = True  # فرض کنید قوانین رعایت شده است

            if is_member and rules_ok:
                return await func(update, context, *args, **kwargs)
            else:
                await update.message.reply_text('❌ شما باید ابتدا در کانال‌ها عضو شوید و قوانین را رعایت کنید.', reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("من هستم", callback_data='join_game')],
                    [InlineKeyboardButton("شروع بازی", callback_data='start_game')]
                ]))
        except httpx.HTTPStatusError as e:
            await update.message.reply_text(f'⚠️ خطایی رخ داد: {e}')
        except Exception as e:
            await update.message.reply_text(f'⚠️ خطای غیرمنتظره‌ای رخ داد: {e}')
    return wrapper

async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    user_name = query.from_user.full_name

    if query.data == 'join_game':
        is_member = await is_user_in_channels(user_id, context)
        if is_member:
            if user_name not in players:
                players.append(user_name)
                await query.edit_message_text(f'بازیکنان: {", ".join(players)}', reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("من هستم", callback_data='join_game')],
                    [InlineKeyboardButton("شروع بازی", callback_data='start_game')]
                ]))
            else:
                await query.answer('شما قبلاً عضو بازی شده‌اید.', show_alert=True)
        else:
            await query.answer('❌ شما باید ابتدا در کانال‌ها عضو شوید.', show_alert=True)
    elif query.data == 'start_game':
        if len(players) >= 2:
            await query.edit_message_text(f'بازی شروع شد! بازیکنان: {", ".join(players)}')
            # شروع بازی
        else:
            await query.answer('هنوز ظرفیت بازی به حد مجاز نرسیده است.', show_alert=True)
