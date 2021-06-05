import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def user_inf(update,context):
    user_id = update.message.chat_id
    text = update.message.text
    f_n = update.message.from_user.first_name
    return  user_id, text, f_n
def start (update, context):
    user_id, text, first_name = user_inf(update,context)
    l = [InlineKeyboardButton(text='Да', callback_data='run')]
    context.bot.send_message(chat_id=user_id, text='Выполнить перезагрузку?',reply_markup=InlineKeyboardMarkup([l]))
def run(update, context):
    os.system("shutdown -t 1 -r -f")
