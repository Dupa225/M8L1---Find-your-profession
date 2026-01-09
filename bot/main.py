import os
from aiogram import Bot, Dispatcher, executor, types
from logic import get_professions_by_answers
from logic import bot_token

BOT_TOKEN = bot_token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

users = {}


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Начать тест")

    await message.answer(
        "Привет! Я помогу выбрать профессию 😎",
        reply_markup=kb
    )

@dp.message_handler(commands=["help"])
async def show_help(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Начать тест")  # кнопка для быстрого старта

    help_text = (
        "🛠 Доступные команды и функции:\n\n"
        "/start - Запуск бота и начало работы\n"
        "Начать тест - Пройти тест для подбора профессии\n"
        "🔄 Пройти тест заново - Сбросить ответы и пройти тест ещё раз\n"
        "/help - Показать это меню\n\n"
        "💡 Как работает тест:\n"
        "1️⃣ Выбираешь категорию (Люди, Числа, Креатив)\n"
        "2️⃣ Выбираешь темп жизни (Спокойный, Средний, Активный)\n"
        "3️⃣ Выбираешь приоритет (Деньги, Свобода, Стабильность, Творчество)\n"
        "Бот подбирает подходящие профессии и кратко описывает их."
    )

    await message.answer(help_text, reply_markup=kb)


@dp.message_handler(lambda m: m.text == "Начать тест")
async def q1(message: types.Message):
    users[message.from_user.id] = {}

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Люди", "Числа")
    kb.add("Креатив")

    await message.answer(
        "Что тебе больше нравится?",
        reply_markup=kb
    )


@dp.message_handler(lambda m: m.text in ["Люди", "Числа", "Креатив"])
async def q2(message: types.Message):
    users[message.from_user.id]["category"] = {
        "Люди": "people",
        "Числа": "numbers",
        "Креатив": "creative",
    }[message.text]

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Спокойный", "Средний", "Активный")

    await message.answer(
        "Какой темп жизни тебе ближе?",
        reply_markup=kb
    )


@dp.message_handler(lambda m: m.text in ["Спокойный", "Средний", "Активный"])
async def q3(message: types.Message):
    users[message.from_user.id]["energy"] = {
        "Спокойный": "low",
        "Средний": "medium",
        "Активный": "high"
    }[message.text]

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Деньги", "Свобода", "Стабильность", "Творчество")

    await message.answer(
        "Что для тебя важнее всего?",
        reply_markup=kb
    )


@dp.message_handler(lambda m: m.text in ["Деньги", "Свобода", "Стабильность", "Творчество"])
async def result(message: types.Message):
    users[message.from_user.id]["goal"] = {
        "Деньги": "money",
        "Свобода": "freedom",
        "Стабильность": "stability",
        "Творчество": "creativity"
    }[message.text]

    u = users[message.from_user.id]

    professions = get_professions_by_answers(
        u["category"],
        u["energy"],
        u["goal"]
    )

    if not professions:
        await message.answer(
            "Хмм, ничего не нашёл 🤔\nПопробуй выбрать другие варианты."
        )
        return

    text = "Вот что тебе может подойти 👇\n\n"
    for name, desc in professions:
        text += f"✅ {name}\n{desc}\n\n"

    await message.answer(text)

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🔄 Пройти тест заново")

    await message.answer(
        "Хочешь попробовать ещё раз или проверить другой вариант? 😉",
        reply_markup=kb
    )


@dp.message_handler(lambda m: m.text == "🔄 Пройти тест заново")
async def restart(message: types.Message):
    users[message.from_user.id] = {}

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Люди", "Числа")
    kb.add("Креатив")

    await message.answer(
        "Погнали заново 😎\nЧто тебе больше нравится?",
        reply_markup=kb
    )


if __name__ == "__main__":
    executor.start_polling(dp)
