import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ContentType
import emoji

def generate_payment_code(user_id: int):
    return f"{user_id}"

logging.basicConfig(level=logging.INFO)

token = "8101029760:AAFu1BUZIzah84YVk_LmcImjHqDQNsZhAGc"

bot = Bot(token=token)
dp = Dispatcher(bot)


# Меню предметов
cheats_menu = ReplyKeyboardMarkup(resize_keyboard=True)
cheats_menu.add(
    KeyboardButton("📘 Английский язык"), KeyboardButton("📗 Русский язык")
).add(
    KeyboardButton("📐 Математика (база)"), KeyboardButton("📊 Математика (профиль)")
).add(
    KeyboardButton("📕 История"), KeyboardButton("🗺️ География")
).add(
    KeyboardButton("📚 Обществознание"), KeyboardButton("💻 Информатика")
).add(
    KeyboardButton("🧬 Биология"), KeyboardButton("⚗️ Химия")
).add(
    KeyboardButton("📖 Литература"), KeyboardButton("🔬 Физика")
)

# Краткие описания предметов
descriptions = {
    "📘 Английский язык": '''Полная подготовка к ЕГЭ: от основ до высокого балла
    ✅ Разбор всех времен (Present Simple → Future Perfect Continuous) с примерами и исключениями.
    ✅ 500+ неправильных глаголов в удобных таблицах и мнемонических схемах.
    ✅ Шаблоны эссе и писем (официальных и неформальных) + разбор критериев оценивания.
    ✅ Аудирование и говорение – тренировка восприятия на слух и правильного произношения.
    ✅ Лайфхаки – как избежать типичных ошибок и сэкономить время на экзамене.

    🔥 Результат: +25-30 баллов за счет четкой структуры и практики!''',
    "📗 Русский язык": '''От орфографии до сочинения: максимум за ЕГЭ
    ✅ Все правила орфографии и пунктуации – разбор сложных случаев (например, «н/нн», «-тся/-ться»).
    ✅ Структура сочинения (К4-К6) – шаблоны, клише, примеры сильных аргументов.
    ✅ Текстовая анализ – как быстро находить проблему, позицию автора и примеры из литературы.
    ✅ Интерактивные диктанты – автоматическая проверка ошибок.
    ✅ Секреты экспертов – какие фразы добавляют баллы.

    🔥 Результат: Минимум 85+ баллов даже при слабой начальной подготовке!''',
    "📐 Математика (база)": '''
    Решаем без ошибок – гарантированный проходной балл!
    ✅ Все формулы и алгоритмы – от процентов до стереометрии.
    ✅ Разбор каждого задания из демоверсий ФИПИ.
    ✅ Тренажер задач – автоматическая генерация вариантов.
    ✅ Ловушки ЕГЭ – какие ошибки допускают 90% учеников.
    ✅ Стратегия решения – как уложиться в время.

    🔥 Результат: 18+ верных ответов из 21!''',
    "📊 Математика (профиль)": '''От простого к сложному: 80+ баллов за ЕГЭ
    ✅ Полный разбор 2-й части – параметры, экономические задачи, стереометрия.
    ✅ Производные и логарифмы – понятные объяснения + 100+ примеров.
    ✅ Геометрия без проблем – векторы, координаты, теоремы.
    ✅ Разбор реальных вариантов 2025 года.
    ✅ Чек-листы – как оформлять, чтобы не сняли баллы.

    🔥 Результат: Решаем 13+ задач из 19 даже без репетитора!''',
    "📕 История": '''Даты, личности, карты – запоминаем навсегда
    ✅ Хронология событий – от Древней Руси до XXI века.
    ✅ Работа с картами и иллюстрациями – как не ошибиться в заданиях.
    ✅ Личности и их роль – кто такой Столыпин и почему он важен?
    ✅ Эссе по истории – план, аргументы, критерии.
    ✅ Тренажер дат – учим без зубрежки.

    🔥 Результат: 90+ баллов за системный подход!''',
    "🗺️ География": '''От климата до экономики: полный охват ЕГЭ
    ✅ Физическая география – рельеф, климат, природные зоны.
    ✅ Экономика регионов – промышленность, сельское хозяйство.
    ✅ Картографический практикум – как читать карты без ошибок.
    ✅ Задания с развернутым ответом – шаблоны для высоких баллов.
    ✅ Актуальная статистика – данные Росстата 2024-2025.

    🔥 Результат: 70+ баллов даже без врожденной «географической жилки»!''',
    "📚 Обществознание": '''Полный разбор кодификатора: от теории до эссе
    ✅ 5 блоков ЕГЭ – экономика, право, политика, социальные отношения, философия.
    ✅ Разбор сложных терминов (например, «инфляция», «правовое государство») на реальных примерах.
    ✅ Шаблоны для мини-сочинения – как раскрыть тему и не потерять баллы.
    ✅ Работа с графиками и схемами – быстрый анализ без ошибок.
    ✅ Актуальные примеры из 2024-2025 года – новые законы, экономические тенденции.

    🔥 Результат: 85+ баллов за четкую структуру и практику!''',
    "💻 Информатика": '''Программирование, логика и алгоритмы – без воды
    ✅ Язык Python для ЕГЭ – разбор всех типов задач (номера 6, 12, 14, 16, 17, 24-27).
    ✅ Работа с таблицами и базами данных – как решать задачи на SQL.
    ✅ Оптимальные алгоритмы – рекурсия, динамическое программирование.
    ✅ Разбор «ловушек» – где чаще всего ошибаются ученики.
    ✅ Автоматическая проверка решений – мгновенная обратная связь.

    🔥 Результат: 90+ баллов даже без углубленного изучения информатики в школе!''',
    "🧬 Биология": '''От клетки до экосистем: вся теория и практика
    ✅ Анатомия и физиология человека – как запомнить все системы за 2 недели.
    ✅ Генетика без страха – алгоритмы решения задач на наследование.
    ✅ Ботаника и зоология – сравнительные таблицы и схемы.
    ✅ Разбор сложных заданий (линия 22, 23, 28) – пошаговый анализ.
    ✅ Тренажер для запоминания терминов – интерактивные карточки.

    🔥 Результат: 80+ баллов за визуализацию и системный подход!''',
    "⚗️ Химия": '''Реакции, задачи и неорганическая химия – просто
    ✅ Разбор всех типов расчетных задач (№29, 30, 34) – молярные массы, выход продукта.
    ✅ Органическая химия – цепочки превращений + механизмы реакций.
    ✅ Таблица Менделеева без зубрежки – лайфхаки для запоминания.
    ✅ Экспериментальные задания – как оформлять выводы.
    ✅ Пробные варианты 2025 года – прогнозируемые изменения.

    🔥 Результат: 75+ баллов даже если химия кажется сложной!''',
    "📖 Литература": '''Анализ текстов, аргументы, исторический контекст
    ✅ Краткие пересказы 100+ произведений – от «Слова о полку Игореве» до Солженицына.
    ✅ Сравнительные таблицы героев – Чацкий vs. Онегин, Раскольников vs. Болконский.
    ✅ Критерии оценивания сочинения – как избежать «воды» и получить максимум.
    ✅ Примеры сильных эссе – разбор работ на 14-15 баллов.
    ✅ Культурный контекст – почему Толстой ненавидел Наполеона?

    🔥 Результат: 80+ баллов за глубокий анализ, а не зазубривание!''',
    "🔬 Физика": '''Формулы, эксперименты и задачи второй части
    ✅ Разбор всех тем кодификатора – механика, термодинамика, оптика, ядерная физика.
    ✅ Лайфхаки для расчетных задач – как подставлять единицы измерения без ошибок.
    ✅ Экспериментальные задания – работа с графиками и приборами.
    ✅ Физические законы в жизни – почему небо голубое и как работает холодильник.
    ✅ Секреты оформления – какие пояснения добавляют баллы.

    🔥 Результат: 75+ баллов за понимание, а не механическое заучивание!'''
}

# Команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    user_info = f"{user.id},{user.username},{user.first_name},{user.last_name}\n"
    
    # Проверяем, был ли уже пользователь записан
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            if str(user.id) not in file.read():
                with open("users.txt", "a", encoding="utf-8") as file_append:
                    file_append.write(user_info)
    except FileNotFoundError:
        # Файл еще не создан
        with open("users.txt", "w", encoding="utf-8") as file:
            file.write(user_info)

    await message.answer('''👋 Привет!
Ты хочешь отлично сдать экзамены и наконец начать студенческую жизнь? 🎓✨
А кто не хочет? 😉

🎯 Давай ближе к делу.
Если ты ещё не начинал подготовку или чувствуешь неуверенность в себе 😟 или пробелы в знаниях 📉,
тебе помогут курсы! 🚀📚

✅ Да, курсы.
Но не обычные, которые пылятся на просторах интернета 🌐🕸,
а специально созданные для выпускников от людей,
которые сами успешно сдали ЕГЭ на 90+ баллов 🧠💯

💡 Они поделятся не только знаниями,
необходимыми для сдачи экзаменов,
но и лайфхаками 🧩, которые помогут быстро усвоить материал
и структурировать уже имеющийся опыт 📖📌

🙌 Если чувствуешь, что такие знания тебе не помешают —
будем рады сопровождать тебя до самих экзаменов! 📆👩‍🏫👨‍🏫

💬 В курс (всего 500 руб) также входит:
— Индивидуальное общение 🗣
— Помощь вплоть до даты экзаменов 🗓💬
— Поддержка без стресса и паники 🧘‍♂️💖

Мы хотим, чтобы ты сдал госэкзамены максимально комфортно
и показал лучшую версию себя на ЕГЭ! 💪🎉

👇 Какой предмет тебе нужен? (Выбери пункт из меню)''', reply_markup=cheats_menu)

# Обработка выбора предмета
@dp.message_handler(lambda message: message.text in descriptions)
async def show_subject_info(message: types.Message):
    subject = message.text
    text = f"{subject}\n\n{descriptions[subject]}\n\nХочешь получить доступ к материалу и наставничество?"
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("💳 Купить", callback_data=f"buy_{subject}"),
    )
    await message.answer(text, reply_markup=keyboard)
def is_emoji(char):
    return char in emoji.EMOJI_DATA
# Обработка inline кнопок
@dp.callback_query_handler(lambda c: c.data.startswith("buy_") or c.data == "back_to_subjects")
async def handle_callbacks(callback: types.CallbackQuery):
    data = callback.data
    subject = data.replace("buy_", "")
    subject = ''.join(char for char in subject if not is_emoji(char))
    if data.startswith("buy_"):
        await bot.send_message(callback.from_user.id, f"💳 Оплата курса + наставничества — 500₽\n\n1️⃣ Переведите 500₽ на карту:\n2200 7004 6065 4543 \n\n2️⃣ В комментарии к платежу укажите:\n{generate_payment_code(callback.from_user.id)}, {subject}\n✍️ (Это важно! Без комментария мы не сможем вас идентифицировать)\n\n3️⃣ После оплаты менеджер свяжется с вами 📲\nи пришлёт все нужные материалы и инструкции 📂✨")


# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
