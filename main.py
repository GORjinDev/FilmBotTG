import asyncio

import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8137773449:AAE5gNNJcT1yXkFWCGJA_sbkDAK-Dnj7se8"
OMDB_API_KEY = "8b93838"

bot = Bot(token=TOKEN)
dp = Dispatcher()

genres = ['action', 'comedy', 'horror']

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Start')]],
    resize_keyboard=True
)

genre_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='action'), KeyboardButton(text='comedy'), KeyboardButton(text='horror')]
    ],
    resize_keyboard=True
)

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот, который помогает найти фильмы 🎬. Напиши мне жанр (например, 'боевик', 'комедия'), и я подберу фильмы!")


@dp.message(lambda message: message.text == 'Start')
async def show_genres(message: types.Message):
    await message.answer("Выбери жанр фильма:", reply_markup=genre_keyboard)


@dp.message(lambda message: message.text in genres)
async def get_movies(message: type.Message):
    genre = message.text
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&s={genre}&type=movie"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            if data.get('Response') == 'True':
                movies = data.get('Search', [])[:5]
                response = f"🎬 Топ фильмов по жанру {genre}:\n\n"
                for movie in movies:
                    response += f"🎞 {movie['Title']} ({movie['Year']})\n"











async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

