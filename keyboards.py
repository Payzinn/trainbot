from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')], 
],
resize_keyboard=True, input_field_placeholder='Вот кнопки')

settings = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/')]
])

another = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Никита', callback_data='nikita')],
    [InlineKeyboardButton(text='Вика', callback_data='vika')],
    [InlineKeyboardButton(text='Корзина', callback_data='cart')],
])

cars = ['Tesla', 'Nikita', 'BMW', 'Lada', 'Жигули', 'Херня']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url = 'https://www.youtube.com/'))
    return keyboard.adjust(2).as_markup()