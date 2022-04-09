import sqlite3

class DB():
    def __DB_connect(self):
        self.db_con = sqlite3.connect('VK_bot.db', check_same_thread=False)
        self.cursor = self.db_con.cursor()


    def __init__(self):
        DB.__DB_connect()
        try:
            create_table_query = '''CREATE TABLE IF NOT EXISTS vk_bot_users (
                                user_id INTEGER PRIMARY KEY UNIQUE,
                                likes INTEGER,
                                dizlikes INTEGER);'''

            self.cursor.execute(create_table_query)
            print("tb create")
            self.bd_con.commit()
            self.cursor.close() 
        
        finally:
            self.db_con.close()
            print("con close")   
    

    def __id_exist(self, id):
        DB.__DB_connect()
        try:
            id_search_query = f"SELECT id FROM vk_bot_users WHERE ID = {id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res != None

        finally:
            self.db_con.close()
            print("id s con close")


    def __update_data(self, user_id, likes, dizlikes):
        DB.__DB_connect()
        try:
            update_query1 = f"UPDATE vk_bot_users SET likes = {likes} WHERE id = {user_id}"
            update_query2 = f"UPDATE vk_bot_users SET dizlikes = {dizlikes} WHERE id = {user_id}"
            self.cursor.execute(update_query1)
            self.cursor.execute(update_query2)
            print("dt upt")
            self.bd_con.commit()
            self.cursor.close()

        finally:
            self.db_con.close()
            print("upd dt con close")

    def search_id(self, id):
        DB.__DB_connect()
        try:
            id_search_query = f"SELECT id FROM vk_bot_users WHERE ID = {id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            print(res)
            self.bd_con.commit()
            self.cursor.close() 
            return res
        
        finally:
            self.db_con.close()
            print("id s con close")  


    def insert_data(self, user_id, likes, dizlikes):
        DB.__DB_connect()
        try:
            if DB.__id_exist():
                insert_query = "INSERT INTO vk_bot_users (user_id, likes, dizlikes) VALUES (%s, %s, %s)"
                self.cursor.execute(insert_query, user_id, likes, dizlikes)
                self.bd_con.commit()
                self.cursor.close()
                print("dt ins ok")
            else:
                DB.__update_data(user_id, likes, dizlikes)
        
        finally:
            self.db_con.close()
            print("dt ins con close") 


    