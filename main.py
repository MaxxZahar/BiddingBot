import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.config import Config, config
from handlers import user, other

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(level=logging.DEBUG, format='%(filename)s:%(lineno)d #%(levelname)-8s '
                         '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')
    
    configuration: Config = config()

    bot = Bot(token=configuration.bot.token)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())