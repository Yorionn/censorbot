import os
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получение переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_USER_ID = int(os.getenv("TARGET_USER_ID", "0"))
KEYWORD = os.getenv("KEYWORD", "").lower()

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен!")

if not TARGET_USER_ID:
    raise ValueError("TARGET_USER_ID не установлен!")

if not KEYWORD:
    raise ValueError("KEYWORD не установлен!")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(F.from_user.id == TARGET_USER_ID)
async def censor_message(message: Message):
    """Удаляет сообщения от целевого пользователя, содержащие ключевое слово"""
    text = message.text or message.caption or ""
    
    if KEYWORD.lower() in text.lower():
        try:
            await message.delete()
            logger.info(f"Удалено сообщение {message.message_id} от пользователя {TARGET_USER_ID}")
        except Exception as e:
            logger.error(f"Ошибка при удалении сообщения: {e}")


async def main():
    logger.info("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

