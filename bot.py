# 1. Импортируем библиотеки
import os
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message               # ловим все обновления этого типа 
from aiogram.filters.command import Command     # обрабатываем команды /start, /help и другие

# 2. Создаем функцию транслитерации текста
def transliterate_text(text: str):
    russian_to_latin = {
    "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D", "Е": "E", "Ё": "E", "Ж": "ZH",
    "З": "Z", "И": "I", "Й": "I", "К": "K", "Л": "L", "М": "M", "Н": "N", "О": "O",
    "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F", "Х": "KH", "Ц": "TS",
    "Ч": "CH", "Ш": "SH", "Щ": "SHCH", "Ы": "Y", "Ъ": "IE", "Э": "E", "Ю": "IU", "Я": "IA"
}

    cyrillic_letters = set("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")

    translit_text = ''

    for i in text.upper():
        if i == 'Ь':
            pass
        elif i == ' ':
            translit_text += ' '
        elif i.isalpha() and i in cyrillic_letters:        
            translit_text += russian_to_latin[i]    
        else: 
            return f'В введеном слове {text} имеются недопустимые символы. Текст должен быть напечатан на кириллице (допускаются пробелы)!' 
            
    return translit_text

# 3. Инициализация объектов
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)   # Создаем объект бота
dp = Dispatcher()                                                   # Создаем объект диспетчера. Все хэндлеры(обработчики) должны быть подключены к диспетчеру
logging.basicConfig(filename='bot.log', level=logging.INFO)         # Указываем в какой файл сохранять логи.

# Домашнее Задание
# - Включить запись log в файл
# - Бот принимает кириллицу отдаёт латиницу в соответствии с Приказом МИД по транслитерации
# - Бот работает из-под docker контейнера

# 4. Обработка/Хэндлер на команду /start
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    time = message.date
    text_for_user = f'Привет {user_name}. Добро пожаловать в сервис транслитерации кириллицы в латиницу в соответствии с Приказом МИД России от 12.02.2020 № 2113. Отправьте текст на кириллице для получения результата.'
    logging.info(f'Пользователь {user_name} {user_id} {time} запустил бота')
    log = f'Пользователь {user_name} {user_id} {time} запустил бота'
    os.system(f'{log} >> logs.txt')

    await bot.send_message(chat_id=user_id, text=text_for_user)

# 5. Обработка/Хэндлер на любые сообщения
@dp.message()
async def transliterate_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    time = message.date
    text_by_user = message.text    
    transliterate_result = transliterate_text(text_by_user)
    logging.info(f'Пользователь {user_name} {user_id} {time} отправил сообщение: {text_by_user}')

    await message.answer(text=transliterate_result)

    logging.info(f'Бот вернул сообщение {transliterate_result} пользователю {user_name} {user_id} {time} с')

# 6. Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)

