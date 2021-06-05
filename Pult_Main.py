from telegram.ext import Updater, Dispatcher, Filters, MessageHandler, CommandHandler, CallbackQueryHandler
from const import TOKEN
from func import *
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(pattern='run', callback=run))
updater.start_polling(drop_pending_updates=True)
updater.idle()
