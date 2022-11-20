from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types
from create_bot import bot, dp
from keyboard import markups
from states import states
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle
from youtube_search import YoutubeSearch
import hashlib

async def start(message: types.Message):
    await bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nНапиши /help')

async def help(message: types.Message):
    await bot.send_message(message.chat.id, 'Я помогу найти тебе музыку, Чтобы найти музыку напиши мое имя и текст\nПример: @shmuzbot моргенштерн')

def searcher(text):
    res = YoutubeSearch(text, max_results=60).to_dict()
    return res

async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    links = searcher(text)

    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title=f'{link["title"]}',
        url=f'https://www.youtube.com/watch?v={link["id"]}',
        thumb_url=f'{link["thumbnails"][0]}',
        input_message_content=types.InputTextMessageContent(
            message_text=f'https://www.youtube.com/watch?v={link["id"]}')
    ) for link in links]

    await query.answer(articles, cache_time=60, is_personal=True)

def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(help, commands='help')
    dp.register_inline_handler(inline_handler)
