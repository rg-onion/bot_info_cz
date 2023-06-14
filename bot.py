import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import mvcr, integration
# Объект бота
from config_reader import token
# from config_reader import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)        # (level=logging.INFO)

# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value()
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=token, parse_mode="HTML")
# bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер
dp = Dispatcher()


# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(mvcr.router)
    dp.include_router(integration.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True, none_stop=True)


if __name__ == "__main__":
    asyncio.run(main())
