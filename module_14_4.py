from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types.callback_query import CallbackQuery

from crud_functions import initiate_db, get_all_products  # Импортируем функции из файла

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = 'token'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных при запуске
initiate_db()  # Создание таблицы, если её ещё нет

# Создание клавиатуры для команды /start
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
start_keyboard.add(button_calculate, button_info, button_buy)

# Создание Inline клавиатуры для покупки продуктов
buying_keyboard = InlineKeyboardMarkup()
for product in get_all_products():  # Создаем кнопки для каждого продукта из базы
    product_id = product[0]
    product_title = product[1]
    buying_keyboard.add(InlineKeyboardButton(product_title, callback_data=f"product_{product_id}"))

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=start_keyboard)

# Обработчик кнопки "Купить"
@dp.message_handler(Text(equals='Купить', ignore_case=True))
async def get_buying_list(message: Message):
    products = get_all_products()  # Получаем список продуктов из базы данных
    for product in products:
        product_id, title, description, price = product
        await message.answer(f"Название: {title}\nОписание: {description}\nЦена: {price} руб.")
    await message.answer("Выберите продукт для покупки:", reply_markup=buying_keyboard)

# Обработчик кнопок в Inline меню для покупки продукта
@dp.callback_query_handler(lambda call: call.data.startswith("product_"))
async def product_purchase(call: CallbackQuery):
    product_id = int(call.data.split("_")[1])  # Извлекаем ID продукта из callback_data
    await call.message.answer(f"Вы выбрали продукт с ID {product_id}. Спасибо за покупку!")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен и готов к работе!")
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Ошибка: {e}")
