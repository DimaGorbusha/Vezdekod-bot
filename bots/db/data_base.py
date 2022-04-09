import sqlite3

class DB():
    def __DB_connect(self):
        self.db_con = sqlite3.connect('VK_bot.db', check_same_thread=False)
        self.cursor = self.db_con.cursor()

    def __init__(self):
        DB.__DB_connect()
        try:
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS vk_bot_memes (
                                user_id INTEGER PRIMARY KEY UNIQUE,
                                dizlikes INTEGER,
                                likes INTEGER);'''
        finally:
            self.bd_con.commit()
            self.bd_con.close()    
    

    def DB_id_search():

    def DB_insert_data():
