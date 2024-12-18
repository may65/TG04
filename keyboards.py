from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Задание 1: Клавиатура с кнопками "Привет" и "Пока"
def get_greeting_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Привет")
    builder.button(text="Пока")
    return builder.as_markup(resize_keyboard=True)

# Задание 2: Инлайн-кнопки с URL-ссылками
def get_links_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Новости", url="https://news.example.com")
    builder.button(text="Музыка", url="https://music.example.com")
    builder.button(text="Видео", url="https://video.example.com")
    return builder.as_markup()

# Задание 3: Динамическая клавиатура
def get_dynamic_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Показать больше", callback_data="show_more")
    return builder.as_markup()

def get_options_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Опция 1", callback_data="option_1")
    builder.button(text="Опция 2", callback_data="option_2")
    return builder.as_markup()