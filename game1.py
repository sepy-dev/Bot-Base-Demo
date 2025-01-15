from telegram import Update
from telegram.ext import CallbackContext
from decorators import check_membership_and_rules

@check_membership_and_rules
async def start_game1(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('بازی 1 شروع شد!')
    # ... کدهای بازی 1 ...
