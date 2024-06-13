from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup
import requests
BOT_TOKEN = "7233493798:AAHbdCudHzqHJiWef3YX9DSA_CojDsXZF3s"
URL = "https://api.thecatapi.com/v1/images/search"

def get_new_img():
    try:
        response = requests.get(URL)
    except Exception as e:
        print(e)
        new_url = "https://api.thedogapi.com/v1/images/search"
    response = requests.get(URL).json()
    randome_cat = response[0]["url"]
    
    return randome_cat
def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_img())

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    
    context.bot.send_message(
        chat_id=chat.id, 
        text="Hello, {}!. Посмотрим котиков".format(name), 
        reply_markup=button) 

def main():
    updater = Updater(token = BOT_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    
    updater.start_polling()
    updater.idle()
    
    
if __name__ == '__main__':
    main()
    
    
    
    