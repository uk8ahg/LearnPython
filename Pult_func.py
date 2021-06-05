from const import *
from time import sleep
import telegram

def start(update,context):
    user_id=update.message.chat_id
    context.bot.send_message(text='Здравствуйте/Salom',chat_id=user_id)
    context.bot.send_message(text='Выберите язык(ru)/Tilni tanlang(uz)',chat_id=user_id)
    textmessage=update.message.text

def text_ansv(update,context):
    flag=False
    user_id = update.message.chat_id
    text_message=update.message.text
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
    if flag==False:
        context.bot.send_message(text = 'Не понял вопроса...', chat_id = user_id)
