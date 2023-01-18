from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import config

bot = Bot(token = config.token)
dp = Dispatcher(bot)

button_backend = KeyboardButton('backend')
button_frontend = KeyboardButton('frontend')
button_uxui = KeyboardButton('uxui')
button_android = KeyboardButton('android')
button_ios = KeyboardButton('ios')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_backend).add(button_frontend).add(button_uxui).add(button_android).add(button_ios)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name}!", reply_markup = greet_kb)

@dp.message_handler(text = ['backend'])
async def backend(message: types.Message):
    await message.reply("""Backend — это внутренняя часть сайта и сервера и т.д
Стоимость 10000 сом в месяц
Обучение: 5 месяц!""")

@dp.message_handler(text = ['frontend'])
async def backend(message: types.Message):
    await message.reply("""frontend — это внешняя часть сайта и сервера и т.д
Стоимость 10000 сом в месяц
Обучение: 5 месяц!""")

@dp.message_handler(text = ['uxui'])
async def backend(message: types.Message):
    await message.reply("""uxui — это часть сайта где создается дизайн и т.д
Стоимость 10000 сом в месяц
Обучение: 5 месяц!""")

@dp.message_handler(text = ['android'])
async def backend(message: types.Message):
    await message.reply("""android — это разработка мобильных приложений(android)
Стоимость 10000 сом в месяц
Обучение: 5 месяц!""")

@dp.message_handler(text = ['ios'])
async def backend(message: types.Message):
    await message.reply("""ios — это разработка мобильных приложений(ios)
Стоимость 10000 сом в месяц
Обучение: 5 месяц!""")


executor.start_polling(dp)
