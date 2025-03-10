import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "YOUR_BOT_TOKEN"  # Укажи свой токен бота
RESUME_PATH = "resume.pdf"  # Укажи путь к резюме (файл должен лежать рядом с bot.py)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Логирование
logging.basicConfig(level=logging.INFO)

# Кнопки с портфолио (замени ссылки на свои)
portfolio_keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton("GitHub", url="https://github.com/your_profile"),
    InlineKeyboardButton("Личный сайт", url="https://yourwebsite.com"),
    InlineKeyboardButton("Пример бота", url="https://t.me/example_bot")
)

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    text = (
        "👋 Привет! Я бот.\n\n"
        "🛠 **Мои навыки:**\n"
        "- Я могу перенаправить тебя на страничку Github моего создателя.\n"
        "- Я могу перенаправить тебя на страничку моего создателя.\n"
        "- Я могу перенаправить тебя на страничку с моим кодом. \n"
    )
    await message.answer(text, reply_markup=portfolio_keyboard)

# Обработчик команды /resume (отправка резюме)
@dp.message_handler(commands=["resume"])
async def send_resume(message: types.Message):
    try:
        with open(RESUME_PATH, "rb") as resume_file:
            await message.answer_document(resume_file, caption="📄 Мое резюме")
    except FileNotFoundError:
        await message.answer("⚠️ Файл резюме не найден. Проверь путь в RESUME_PATH.")

# Запуск бота
async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
