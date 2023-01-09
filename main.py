'''Прикрутить бота: Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, 
добавив в неё систему логирования'''

import Logger
import Arithmetic
import Complex
from telebot import TeleBot, types


TOKEN = '5877473521:AAHc3V_zEdeoD-tTrSfTfrZ5z8clHAjbBsM'


bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Здравствуйте! Введите арифметическое выражение: \n\
(Возведение в степень укажите как "^", а корень словом "root")\n')
    bot.register_next_step_handler(msg, start)


@bot.message_handler(commands=['logger'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Файл логгирования')
    with open('log.csv', 'rb') as f:
        bot.send_document(msg.from_user.id, f)
    bot.register_next_step_handler(msg, start)


def start(message):
    operation = message.text
    Logger.logger(operation, 'entered data is')
    if 'j' in operation:
        operation = Complex.to_complex(operation)
        bot.reply_to(message, text=f'{operation}')

    elif '+' in operation:
        operation = Arithmetic.addition(operation)
        bot.reply_to(message, text=f'{operation}')

    elif '-' in operation:
        operation = Arithmetic.subtract(operation)
        bot.reply_to(message, text=f'{operation}')

    elif '*' in operation:
        operation = Arithmetic.multiply(operation)
        bot.reply_to(message, text=f'{operation}')

    elif '/' in operation:
        operation = Arithmetic.division(operation)
        bot.reply_to(message, text=f'{operation}')

    elif '^' in operation:
        operation = Arithmetic.exponent(operation)
        bot.reply_to(message, text=f'{operation}')

    elif 'root' in operation:
        operation = Arithmetic.root(operation)
        bot.reply_to(message, text=f'{operation}')
        # bot.send_message(chat_id=message.from_user.id, text=f'{operation}')
        # return Arithmetic.root(operation)
    repeat(message)


@bot.message_handler()
def repeat(msg: types.Message):
    bot.register_next_step_handler(msg, start)


# print(start())
bot.polling()
