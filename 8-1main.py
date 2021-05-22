from telegram.ext import Updater, Dispatcher, Filters, MessageHandler, CommandHandler, CallbackQueryHandler
from const import TOKEN
from func import *
updater = Updater(token=TOKEN, workers = 5)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(pattern='uzb', callback=uzb))
dispatcher.add_handler(CallbackQueryHandler(pattern='rus', callback=rus))
dispatcher.add_handler(MessageHandler(filters = Filters.text,callback = text_ansv,run_async = True))

updater.start_polling(drop_pending_updates=True)
updater.idle()
