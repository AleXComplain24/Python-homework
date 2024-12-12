from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = 'Token'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Класс состояний пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    # Создание клавиатуры
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = KeyboardButton('Рассчитать')
    button_info = KeyboardButton('Информация')
    keyboard.add(button_calculate, button_info)

    # Отправка приветственного сообщения с клавиатурой
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=keyboard)

# Функция начальной команды для ввода возраста
@dp.message_handler(Text(equals='Рассчитать', ignore_case=True))
async def set_age(message: Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

# Функция для обработки возраста и перехода к вводу роста
@dp.message_handler(state=UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

# Функция для обработки роста и перехода к вводу веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

# Функция для обработки веса и вычисления нормы калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Упрощённая формула Миффлина-Сан Жеора для мужчин
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {bmr:.2f} калорий в день.")
    await state.finish()

# Обработчик кнопки "Информация"
@dp.message_handler(Text(equals='Информация', ignore_case=True))
async def info(message: Message):
    await message.answer("Этот бот помогает вычислить вашу норму калорий. Нажмите 'Рассчитать', чтобы начать.")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен и готов к работе!")
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        print(f"Ошибка: {e}")

