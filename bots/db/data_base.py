import sqlite3

class DB():
    def __DB_connect(self):
        self.db_con = sqlite3.connect('VK_bot.db', check_same_thread=False)
        self.cursor = self.db_con.cursor()

    def __init__(self):
        DB.__DB_connect()
        try:
            create_table_query = '''CREATE TABLE IF NOT EXISTS vk_bot_memes (
                                user_id INTEGER PRIMARY KEY UNIQUE,
                                dizlikes INTEGER,
                                likes INTEGER);'''

            self.cursor.execute(create_table_query)
            print("tb create")
            self.bd_con.commit()
            self.cursor.close() 

        finally:
            self.db_con.close()
            print("con close")   
    

    def DB_id_search():
        DB.__DB_connect()

    def DB_insert_data():

    def DB_update_data():
