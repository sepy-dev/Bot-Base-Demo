# 🤖 Telegram Inline Game Bot with Membership Check DEMO

A Python-powered Telegram bot that can be used **inline** in any private or group chat. Before starting the game, it checks if the user is a member of a specific channel — no errors if they are, just pure fun! 🎮

---

## 🌟 Features

- ✅ Built with `python-telegram-bot`
- 🧠 Custom **decorator** for membership checking
- 📱 Supports **inline mode** — trigger the bot in any chat by searching its username
- 🔒 Only starts the game if the user is a member of the specified channel
- 💬 Sends invitation to join if the user isn't a member

---

## 🔧 How It Works

1. The user types the bot's username in any chat.
2. The bot checks whether the user is subscribed to a given channel.
3. If not, it sends a message with a channel invite.
4. If yes, the game starts immediately with no delay.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `python-telegram-bot` v20+

### Installation

```bash
https://github.com/sepy-dev/Meme-Bot.git
cd Meme-Bot.git


Configuration

Create a main.py file and set your bot token and required channel:

TOKEN = 'your-bot-token-here'
REQUIRED_CHANNEL_ID = '@your_channel'

Running the Bot

python main.py

🗂 Project Structure

📁 your-bot-name/
├── bot.py              # Main bot file
├── decorators.py       # Membership checking decorator
├── handlers.py         # Game/message handlers
├── config.py           # Token and settings
├── requirements.txt    # Required packages
└── README.md           # This file

📸 Preview

    (Add a screenshot or demo GIF of your bot in action here)

📄 License

Released under the MIT License.
🙋‍♂️ Contributions

Contributions are welcome! Open an issue or pull request to suggest improvements. Happy coding! ❤️
ربات تلگرام اینلاین با بررسی عضویت دمو

رباتی ساده و کاربردی که با پایتون نوشته شده و به‌صورت اینلاین در هر چت (خصوصی یا گروهی) قابل استفاده است. قبل از شروع بازی، بررسی می‌کند که آیا کاربر عضو کانال خاصی هست یا نه. اگر عضو باشد، بازی بدون خطا شروع می‌شود! 🎯
🌟 ویژگی‌ها

    ✅ نوشته‌شده با استفاده از python-telegram-bot

    🧠 دکوراتور اختصاصی برای بررسی عضویت کاربر

    💬 پشتیبانی از حالت اینلاین (فراخوانی ربات در هر چت)

    🔒 شروع بازی تنها در صورت عضویت در کانال مشخص‌شده

    📩 ارسال پیام دعوت در صورت عدم عضویت

🧩 نحوه عملکرد

    کاربر در هر چت، نام ربات را جستجو می‌کند.

    ربات عضویت در کانال تعیین‌شده را بررسی می‌کند.

    اگر عضو نباشد، لینک عضویت ارسال می‌شود.

    اگر عضو باشد، بازی بدون تأخیر شروع می‌شود.

⚙️ شروع سریع
پیش‌نیازها

    پایتون نسخه 3.8 به بالا

    کتابخانه python-telegram-bot نسخه 20+

نصب

git clone https://github.com/your-username/your-bot-name.git
cd your-bot-name
pip  python-telegram-bot

تنظیمات

فایلی به نام main.py بسازید و اطلاعات زیر را وارد کنید:

TOKEN = 'توکن ربات شما'


اجرای ربات

python main.py

🗂 ساختار پروژه

📁 your-bot-name/
├── bot.py              # فایل اصلی ربات
├── decorators.py       # دکوراتور بررسی عضویت
├── handlers.py         # هندلر پیام‌ها و بازی
├── config.py           # توکن و اطلاعات کانال
├── requirements.txt    # کتابخانه‌های موردنیاز
└── README.md           # این فایل

📷 پیش‌نمایش

    (در این بخش می‌تونی تصویر یا ویدیویی از عملکرد رباتت بذاری)

📜 مجوز

این پروژه تحت مجوز MIT License منتشر شده است.
🧠 همکاری و مشارکت

اگر پیشنهاد یا مشکلی داری، با خیال راحت یک Issue باز کن یا Pull Request بفرست. با هم بهترش می‌کنیم! 🌱
