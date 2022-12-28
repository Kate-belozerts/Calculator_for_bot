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


def start(message):
    operation = message.text
#operation = input('Введите арифметическое выражение: \n\
#(Возведение в степень укажите как "^", а корень словом "root")\n')
    Logger.logger(operation, 'entered data is')
    if 'j' in operation:
        operation = Complex.to_complex(operation)
        bot.send_message(chat_id=message.from_user.id, text=f'{operation}')
        # return operation

    elif '+' in operation:
        operation = Arithmetic.addition(operation)
        bot.send_message(chat_id=message.from_user.id, text=f'{operation}')
        # return operation

    elif '-' in operation:
        operation = Arithmetic.subtract(operation)
        bot.send_message(chat_id=message.from_user.id, text=f'{operation}')
        # return Arithmetic.subtract(operation)

    elif '*' in operation:
        operation = Arithmetic.multiply(operation)
        bot.send_message(chat_id=message.from_user.id, text=f'{operation}')
        # return Arithmetic.multiply(operation)

    elif '/' in operation:
        operation = Arithmetic.division(operation)
        bot.send_message(chat_id=message.from_user.id, text=f'{operation}')
        # return Arithmetic.division(operation)

    elif '^' in operation:
        operation = Arithmetic.exponent(operation)
        bot.send_message(chat_id=message.from_user.id, text=f'{operation}')
        # return Arithmetic.exponent(operation)

    elif 'root' in operation:
        operation = Arithmetic.root(operation)
        bot.send_message(chat_id=message.from_user.id, text=f'{operation}')
        # return Arithmetic.root(operation)
    to_continue(message)


def to_continue(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Хотите ввести еще одно выражение?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: call.data == 'yes')
    def call_back(call):
        bot.send_message(chat_id=call.from_user.id, text='Хорошо, давайте продолжим?')

        @bot.message_handler(content_types=['text'])
        def get_text_messages(msg):
            bot.send_message(chat_id=msg.from_user.id, text='Нужно ввести арифметическое выражение: \n\
(Возведение в степень укажите как "^", а корень словом "root")\n')
            bot.register_next_step_handler(msg, start)

    @bot.callback_query_handler(func=lambda call: call.data == 'no')
    def call_back(call):
        bot.send_message(chat_id=call.from_user.id, text=f'Хорошо, закончим на сегодня. До свидания!)')


# print(start())
# start()
bot.polling()
