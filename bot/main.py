from telebot import TeleBot ,types
from telebot.types import Message,User
from db import db
@bot.ChatjoinRequest_handler(func=lambda ChatjoinRequest : True)
def send_message(ChatjoinRequest):
    try:
        db=db.db()
        db.insert(ChatjoinRequest.user_chat_id)
    except Exception as e:
        print(e)
    bot.send_message(ChatjoinRequest.user_chat_id,"hi")
@bot.message_handler(func=lambda message:True)
def send_all(message):
    if message.from_user=="":
        db=db.db()
        chats=db.get_chats_chats()
        i=0
        for chat in chats:
            try:
                bot.send_message(chat.chat_id,text)
                i=i+1
            except Exception as e:
                print(e)
        stp="message send to"+ i +"peoples "
        try:
            bot.send_message(message.from_user, stp) 
        except Exception as e:
            print(e)          