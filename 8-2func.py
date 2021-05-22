import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from sql_req import *
from const import *
from time import sleep
def user_inf(update,context):
    user_id = update.message.chat_id
    text = update.message.text
    f_n = update.message.from_user.first_name
    return  user_id, text, f_n

def start ( update , context):
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    user_id, text, first_name = user_inf(update,context)
    cursor.execute(reg_in_table.format(user_id,first_name))
    conn.commit()
    b = [
        InlineKeyboardButton(text='Uzb', callback_data='uzb'),
        InlineKeyboardButton(text='Rus', callback_data='rus')]
    context.bot.send_message(chat_id=user_id, text='Выберите язык:',reply_markup=InlineKeyboardMarkup([b]))

def uzb(update,context):
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    user_id = update.callback_query.from_user.id
    cursor.execute(update_lang_in_table.format(1,user_id))
    conn.commit()
    context.bot.send_message(text='Ozbek tili', chat_id=user_id)
    l = cursor.execute(lang_in_table.format(user_id)).fetchall()
    l = l[0][0]
    context.bot.send_message(text=GLOBAL_DCT.get(l)[0], chat_id = user_id)

def rus(update,context):
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    user_id = update.callback_query.from_user.id
    cursor.execute(update_lang_in_table.format(2, user_id))
    conn.commit()
    context.bot.send_message(text='Русский язык', chat_id=user_id)
    l = cursor.execute(lang_in_table.format(user_id)).fetchall()
    l = l[0][0]
    context.bot.send_message(text=GLOBAL_DCT.get(l)[0], chat_id = user_id)

def get_lang(update,context):
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    user_id = update.message.chat_id
    a=cursor.execute(lang_in_table.format(user_id)).fetchall()
    conn.commit()
    return a

def text_ansv(update,context):
    flag=False
    b=get_lang(update,context)
    b = b[0][0]
    user_id = update.message.chat_id
    text_message=update.message.text
    if b==2:
        for e in DICT_QUEST:
            lstQ = DICT_QUEST.get(e)
            if text_message in lstQ:
                lstA=DICT_ANS.get(e)
                A=lstA[0]
                context.bot.send_chat_action(chat_id=user_id,action=telegram.ChatAction.TYPING)
                sleep(2)
                context.bot.send_message(text=A,chat_id=user_id)
                flag=True
                break
    elif b==1:
        for e in DICT_QUEST:
            lstQ = DICT_QUEST.get(e)
            if text_message in lstQ:
                lstA=DICT_ANS.get(e)
                A=lstA[1]
                context.bot.send_chat_action(chat_id=user_id,action=telegram.ChatAction.TYPING)
                sleep(2)
                context.bot.send_message(text=A,chat_id=user_id)
                flag=True
                break
    if flag==False and b==2:
        context.bot.send_message(text = 'Не понял вопроса...', chat_id = user_id)
    elif flag==False and b==1:
        context.bot.send_message(text = 'Savolni tushumadim...' , chat_id = user_id)
