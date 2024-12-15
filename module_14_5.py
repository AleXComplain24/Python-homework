from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.types.callback_query import CallbackQuery

from crud_functions import initiate_db, get_all_products, add_user, is_included  # Импортируем функции из файла

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = 'token'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Инициализация базы данных при запуске
initiate_db()

# Обновляем клавиатуру для главного меню
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
button_register = KeyboardButton('Регистрация')  # Новая кнопка
start_keyboard.add(button_calculate, button_info, button_buy, button_register)

# Машина состояний для регистрации
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=start_keyboard)

# Обработчик кнопки "Регистрация"
@dp.message_handler(Text(equals='Регистрация', ignore_case=True))
async def sign_up(message: Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

# Сохранение имени пользователя
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    username = message.text
    if is_included(username):  # Проверяем, есть ли пользователь в таблице
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

# Сохранение email пользователя
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

# Сохранение возраста пользователя и завершение регистрации
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 0:
            raise ValueError
        await state.update_data(age=age)

        # Получаем данные из состояния
        data = await state.get_data()
        username = data['username']
        email = data['email']

        # Добавляем пользователя в таблицу
        add_user(username, email, age)
        await message.answer("Вы успешно зарегистрированы! Ваш баланс: 1000 руб.")
        await state.finish()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст (число).")

# Обработчик кнопки "Купить"
@dp.message_handler(Text(equals='Купить', ignore_case=True))
async def get_buying_list(message: Message):
    products = get_all_products()  # Получаем список продуктов из базы данных
    for product in products:
        product_id, title, description, price = product
        await message.answer(f"Название: {title}\nОписание: {description}\nЦена: {price} руб.")
    await message.answer("Выберите продукт для покупки:")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен и готов к работе!")
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Ошибка: {e}")
