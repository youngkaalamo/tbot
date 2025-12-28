from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from recommender.data_loader import load_data
from recommender.preprocess import preprocess_dataframe
from recommender.model import Recommender
from bot.keyboards import main_menu_keyboard
from config import DATA_PATH, TOP_N_RECOMMENDATIONS

router = Router()
df = load_data(DATA_PATH)
df = preprocess_dataframe(df)
recommender = Recommender(DATA_PATH)


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Привет! 🎬\n"
        "Я рекомендательный бот по фильмам.\n\n"
        "Используй команду:\n"
        "/recommend <название фильма>\n"
        "/random",
        reply_markup=main_menu_keyboard()
    )


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "/recommend <название> — рекомендации по фильму\n"
        "/random — случайный фильм"
    )


@router.message(Command("recommend"))
async def recommend_handler(message: Message):
    query = message.text.replace("/recommend", "").strip()

    if not query:
        await message.answer("Пожалуйста, укажи название фильма.")
        return

    result = recommender.recommend(query, TOP_N_RECOMMENDATIONS)

    # Если вернулась строка — это ошибка
    if isinstance(result, str):
        await message.answer(result)
        return

    response = "🎬 Рекомендованные фильмы:\n\n"
    for movie in result:
        response += f"• {movie['title']}\n"

    await message.answer(response)


@router.message(Command("random"))
async def random_handler(message: Message):
    movies = recommender.get_random(1)
    movie = movies[0]

    await message.answer(
        f"🎲 Случайный фильм:\n\n"
        f"{movie['title']}\n"
        f"{movie['description']}"
    )
