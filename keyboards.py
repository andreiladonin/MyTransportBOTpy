from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = ReplyKeyboardMarkup()

stops = KeyboardButton("Остановки 🚍")

main_keyboard.add(stops)

stop_keyboard = ReplyKeyboardMarkup()

list_stop = KeyboardButton("Магазин 🚍")

stop_keyboard.add(list_stop)