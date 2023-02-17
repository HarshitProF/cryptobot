import sqlite3
class db:
    def __init__(self):
        self.conn=sqlite3.connect("my.db")
        cursor=self.conn.cursor()
        #cursor.execute('drop table chats')
        cursor.execute("create table if NOT EXISTS chats ( chat_id int UNIQUE)")
    def insert(self,chats_id):
        cursor=self.conn.cursor()
        query="insert into chats (chat_id ) VALUES (?)"
        print(chats_id)
        val=(chats_id,)
        try:
            cursor.execute(query,val)
        except Exception as e:
            print(e)
        try:
            self.conn.commit()
        except Exception as e:
            print(e)
        
    def get_chats(self):
        cursor=self.conn.cursor()
        query="select * from chats"
        cursor.execute(query)
        chat_ids=cursor.fetchall()
        print(chat_ids)
        return chat_ids
