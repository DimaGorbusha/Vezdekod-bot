import sqlite3

class DB():
    def __DB_connect(self):
        self.db_con = sqlite3.connect('VK_bot.db', check_same_thread=False)
        self.cursor = self.db_con.cursor()


    def __init__(self):
        self.__DB_connect()
        print("всё ок")
        try:
            create_table_query = '''CREATE TABLE IF NOT EXISTS vk_bot_users (
                                user_id INTEGER PRIMARY KEY UNIQUE,
                                likes INTEGER,
                                dizlikes INTEGER);'''

            self.cursor.execute(create_table_query)
            print("tb create")
            self.db_con.commit()
            self.cursor.close() 
        
        finally:
            self.db_con.close()
            print("con close")   
    

    def __id_exist(self, id):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT user_id FROM vk_bot_users WHERE user_id = {id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res != None

        finally:
            self.db_con.close()
            print("id s con close")


    def __update_data(self, user_id, likes, dizlikes):
        self.__DB_connect()
        try:
            update_query1 = f"UPDATE vk_bot_users SET likes = {likes} WHERE user_id = {user_id}"
            update_query2 = f"UPDATE vk_bot_users SET dizlikes = {dizlikes} WHERE user_id = {user_id}"
            self.cursor.execute(update_query1)
            self.cursor.execute(update_query2)
            print("dt upt")
            self.db_con.commit()
            self.cursor.close()

        finally:
            self.db_con.close()
            print("upd dt con close")


    def search_id(self, id):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT user_id FROM vk_bot_users WHERE user_id = {id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            print(res)
            self.db_con.commit()
            self.cursor.close() 
            return res
        
        finally:
            self.db_con.close()
            print("id s con close")  


    def get_likes(self, user_id):
        pass

    def get_dizlikes(self, user_id):
        pass

    def insert_data(self, user_id, likes, dizlikes):
        self.__DB_connect()
        try:
            if self.__id_exist(user_id):
                insert_query = "INSERT INTO vk_bot_users (user_id, likes, dizlikes) VALUES (%s, %s, %s)"
                self.cursor.execute(insert_query, user_id, likes, dizlikes)
                self.db_con.commit()
                self.cursor.close()
                print("dt ins ok")
            else:
                self.__update_data(user_id, likes, dizlikes)
        
        finally:
            self.db_con.close()
            print("dt ins con close") 


    