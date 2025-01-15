from telegram.ext import Application, CommandHandler

from handlers import start  # اضافه کردن هندلرهای جدید


async def main():
    application = Application.builder().token("7847166209:AAFfQLo46-rMVJxfuL9MxXNM-QzP3nKUn5g").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))

    # Start the application
    await application.start()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
