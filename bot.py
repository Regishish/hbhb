import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from datetime import datetime, timedelta

API_TOKEN = '7925037089:AAERkJTfPuTwoExW3bysZQyf9f7WfjTsdXE'
USER_ID = 7925037089

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопка старта
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(KeyboardButton("Приступить"))

# Комплименты каждый час
compliments = [
    "Ты — моя опора 💪",
    "Ты — мой самый лучший человек на свете 🌍",
    "С тобой не страшно ни одно испытание 🛡",
    "Ты умеешь сделать меня счастливой просто своим взглядом 😊",
    "Ты вдохновляешь и поддерживаешь, когда я сама падаю духом 🕊",
    "Ты самый умный и сильный мужчина в мире 💼",
    "Ты — спокойствие среди моего урагана 🌀",
    "Ты смешной, добрый и очень красивый 😍",
    "Ты умеешь делать вкусный кофе и хорошее настроение ☕",
    "Ты — мой дом 🏠",
    "Ты умеешь любить — по-настоящему 💖",
    "Ты лучшее, что случилось со мной ✨",
]

# Основной квест
tasks = [
    "🎉 С днём рождения! Сегодня тебя ждёт игра! В конце — подарок 🎁. Начнём!",
    "🍳 Задание 1: Вкусный завтрак. Сфоткай его и отправь мне 📸",
    "🎂 Задание 2: Задуй свечу и загадай желание ✨",
    "🏖 Задание 3: Фото из моря или бассейна. Лицо — безумно счастливое 😄",
    "🍹 Задание 4: Время напитков. Пиво, негрони, чай или вода — с тебя селфи!",
    "🍽 Задание 5: Выбери ресторан: 1) Восточный квартал, 2) СанРемо, 3) Плакучая Ива, 4) Чита-Маргарита, 5) Реззо, 6) Свой вариант",
    "📝 Задание 6: Пройди мини-опрос! 🎯 (команда /quiz)",
    "🎁 Задание 7: Обними жену и получи подарок ❤️",
]

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id == USER_ID:
        await message.answer("Готов начать день рождения?", reply_markup=start_kb)

@dp.message_handler(Text(equals="Приступить"))
async def start_game(message: types.Message):
    if message.from_user.id == USER_ID:
        for task in tasks:
            await message.answer(task)
            await asyncio.sleep(300)  # 5 минут между заданиями

@dp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    if message.from_user.id == USER_ID:
        await message.answer("🎯 Опрос: «Проверим, насколько ты хорошо знаешь нас»")
        # Вопросы отправляются один за другим
        await message.answer("1️⃣ Что мы делаем слишком часто, а я всегда не против?

"
                             "A) Путешествуем ✅
B) Едим
C) Спим
D) Сам знаешь что…")

        await asyncio.sleep(10)
        await message.answer("2️⃣ Какой мой любимый сериал для уборки?

"
                             "A) Секс в большом городе
B) Оленёнок
C) Отчаянные домохозяйки ✅
D) Игра престолов")

        await asyncio.sleep(10)
        await message.answer("3️⃣ Что ты чаще всего говоришь утром?

"
                             "A) Доброе утро, любимая
B) Сколько время?
C) Не трогай меня ✅
D) Я уже сделал кофе")

        await asyncio.sleep(10)
        await message.answer("4️⃣ Где чаще всего оказываются твои носки?

"
                             "A) В бельевом ящике
B) На сушилке
C) В зале в углу ✅
D) Ты что, я их всегда убираю")

        await asyncio.sleep(10)
        await message.answer("5️⃣ Кто просыпается раньше?

"
                             "A) Ты
B) Я
C) Оба одновременно
D) Всё зависит от случая ✅")

        await asyncio.sleep(10)
        await message.answer("6️⃣ Что любит твоя жена, а ты не очень?

"
                             "A) Пляжный отдых
B) Турецкие сериалы ✅
C) Завтрак в ресторане
D) Пешие прогулки")

        await asyncio.sleep(10)
        await message.answer("7️⃣ За что твоя жена тебя больше всего любит?

"
                             "A) За заботу
B) За чувство юмора
C) За доброту
D) За всё это вместе ✅")

        await asyncio.sleep(10)
        await message.answer("8️⃣ Твоя суперспособность — это:

"
                             "A) Видеть хаос и оставаться спокойным
B) Быть мужчиной мечты
"
                             "C) Находить вкусную еду
D) Занимать всю кровать
E) ✅ Всё вместе")

        await asyncio.sleep(10)
        await message.answer("9️⃣ Чем ты гордишься в себе больше всего?

"
                             "A) Умом
B) Спокойствием
C) Силой
Ответ: А надо всем вместе 💪🧠🧘‍♂️")

        await asyncio.sleep(10)
        await message.answer("🔟 Куда мы точно никогда не поедем в отпуск?
(Ответь сам)
➡️ Это я так, справочно 😉")

        await asyncio.sleep(5)
        await message.answer("🎉 Поздравляю, ты прошёл опрос!
Ты почти у цели… Скоро тебя ждёт кое-что очень приятное 🎁❤️")

async def send_compliments():
    while True:
        now = datetime.now()
        if now.hour in range(9, 21) and now.minute == 30:
            compliment = compliments[(now.hour - 9) % len(compliments)]
            await bot.send_message(USER_ID, f"💬 {compliment}")
        await asyncio.sleep(60)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(send_compliments())
    executor.start_polling(dp, skip_updates=True)