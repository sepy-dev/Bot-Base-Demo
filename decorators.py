from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import httpx
from users import is_user_in_channels  # اضافه کردن تابع بررسی عضویت

players = []

def check_membership_and_rules(keygame):
    def decorator(func):
        async def wrapper(update: Update, context: CallbackContext, *args, **kwargs):
            try:
                query = update.callback_query
                user_id = query.from_user.id
                user_name = query.from_user.full_name    
                # تعریف متغیر keygame
                print(f"Callback data: {query.data}")  # Debugging statement
                print(f"Expected keygame: {keygame}")  # Debugging statement
                if query.data == keygame:
                    await query.edit_message_text(f'بازیکنان: {", ".join(players)}', reply_markup=InlineKeyboardMarkup([
                                [InlineKeyboardButton("من هستم", callback_data=f'{keygame}_join_game')],
                                [InlineKeyboardButton("شروع بازی", callback_data=f'{keygame}_start_game')]
                            ]))
                elif query.data == f'{keygame}_join_game':
                    print(f"Join game detected for keygame: {keygame}")  # Debugging statement
                    is_member = await is_user_in_channels(user_id, context)
                    if is_member:
                        if user_name not in players:
                            players.append(user_name)
                        await query.edit_message_text(f'بازیکنان: {", ".join(players)}', reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton("من هستم", callback_data=f'{keygame}_join_game')],
                            [InlineKeyboardButton("شروع بازی", callback_data=f'{keygame}_start_game')]
                        ]))
                    else:
                        await query.answer('❌ شما باید ابتدا در کانال‌ها عضو شوید.', show_alert=True)
                elif query.data == f'{keygame}_start_game':
                    if len(players) >= 2:
                        await query.edit_message_text(f'بازی شروع شد! بازیکنان: {", ".join(players)}')

                await func(update, context, keygame=keygame, *args, **kwargs)

            except httpx.HTTPStatusError as e:
                if update.message:
                    await update.message.reply_text(f'⚠️ خطایی رخ داد: {e}')
                else:
                    await update.callback_query.message.reply_text(f'⚠️ خطایی رخ داد: {e}')
            except Exception as e:
                if update.message:
                    await update.message.reply_text(f'⚠️ خطای غیرمنتظره‌ای رخ داد: {e}')
                else:
                    await update.callback_query.message.reply_text(f'⚠️ خطای غیرمنتظره‌ای رخ داد: {e}')
        return wrapper
    return decorator


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
    elif query.data == 'about_us':
        await query.edit_message_text('این ربات برای بازی و سرگرمی طراحی شده است. از بازی‌ها لذت ببرید!')
