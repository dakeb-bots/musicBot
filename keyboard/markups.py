from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def search():
    btn_search = InlineKeyboardButton(text='Найти', callback_data='search')
    markup_search = InlineKeyboardMarkup()
    markup_search.add(btn_search)

    return markup_search
