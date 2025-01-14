from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from users import start_user_management

async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    start_user_management(application)

    await application.start()
    await application.start_polling()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
    #sss
