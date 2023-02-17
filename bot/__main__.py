from . import bot
from telebot.types import Message,User
from db import db
@bot.chat_join_request_handler(func=lambda ChatjoinRequest : True)
def send_message(ChatjoinRequest):
    try:
        db.db().insert(ChatjoinRequest.user_chat_id)
    except Exception as e:
        print(e)
    bot.send_message(ChatjoinRequest.user_chat_id,"hi")
@bot.message_handler(func=lambda message:True)
def send_all(message):
    text=message.text
    if message.chat.id==741728025:
        chats=db.db().get_chats()
        print(chats)
        i=0
        j=0
        k=0
        for chat in chats:
            print(chat[i])
            try:
                bot.send_message(chat[i],text)
                k=k+1
            except Exception as e:
                print(e)
            j=j+1
        resulted=f"message sent to{k+1} people out of {j+1} people"
        bot.send_message(message.chat.id, resulted)
bot.infinity_polling()