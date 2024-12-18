import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Задание 1: Обработка команды /start
@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("Выберите опцию:", reply_markup=kb.get_greeting_keyboard())

@dp.message(lambda message: message.text == "Привет")
async def greet_user(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")

@dp.message(lambda message: message.text == "Пока")
async def farewell_user(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}!")

# Задание 2: Обработка команды /links
@dp.message(Command(commands=["links"]))
async def send_links(message: Message):
    await message.answer("Выберите ссылку:", reply_markup=kb.get_links_keyboard())

# Задание 3: Обработка команды /dynamic и динамическое изменение клавиатуры
@dp.message(Command(commands=["dynamic"]))
async def send_dynamic_keyboard(message: Message):
    await message.answer("Выберите опцию:", reply_markup=kb.get_dynamic_keyboard())

@dp.callback_query(lambda c: c.data == "show_more")
async def show_more_options(callback_query: CallbackQuery):
    await callback_query.message.edit_reply_markup(reply_markup=kb.get_options_keyboard())

@dp.callback_query(lambda c: c.data in ["option_1", "option_2"])
async def handle_option(callback_query: CallbackQuery):
    option = "Опция 1" if callback_query.data == "option_1" else "Опция 2"
    await callback_query.answer(f"Вы выбрали {option}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())