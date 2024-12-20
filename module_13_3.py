from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = 'YOUR_BOT_TOKEN'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    # Отправляем ответ в Telegram с использованием метода answer
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")

# Обработчик всех остальных сообщений
@dp.message_handler()
async def all_messages(message: Message):
    # Отправляем ответ в Telegram с использованием метода answer
    await message.answer("Введите команду /start, чтобы начать общение.")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен и готов к работе!")
    executor.start_polling(dp, skip_updates=True)
