from telegram.ext import Updater,CommandHandler, MessageHandler,Filters
from const import *
from func import *
updater=Updater(token=TOKEN,workers=5)
dispacher=updater.dispatcher
dispacher.add_handler(CommandHandler(command = 'start',callback = start,run_async = True))
dispacher.add_handler(MessageHandler(filters = Filters.text,callback = text_ansv,run_async = True))
updater.start_polling(drop_pending_updates = True)
