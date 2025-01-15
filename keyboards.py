from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_game_keyboard():
    keyboard = [
        [InlineKeyboardButton("شروع بازی 1", callback_data='inline_game1_start')],
        [InlineKeyboardButton("شروع بازی 2", callback_data='inline_game2_start')],
        [InlineKeyboardButton("شروع بازی 3", callback_data='inline_game3_start')],
        [InlineKeyboardButton("شروع بازی 4", callback_data='inline_game4_start')]
    ]
    return InlineKeyboardMarkup(keyboard)
