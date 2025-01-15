from telegram.ext import ContextTypes, Application

print("users.py has been imported")

# کانال‌هایی که باید عضو شوند
required_channels = ["@YourChannel1", "@YourChannel2"]

# بررسی عضویت کاربر در کانال‌ها
async def is_user_in_channels(user_id, context: ContextTypes.DEFAULT_TYPE):
    for channel in required_channels:
        try:
            member = await context.bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False
    return True

def start_user_management(application: Application):
    # کد مربوط به مدیریت کاربران را اینجا اضافه کنید
    pass
