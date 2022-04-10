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
    

    def __id_exist(self, user_id):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT user_id FROM vk_bot_users WHERE user_id = {user_id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res != None
        finally:
            self.db_con.close()
            print("id s con close")


    def __get_likes(self, user_id):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT likes FROM vk_bot_users WHERE user_id = {user_id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res
        finally:
            self.db_con.close()
            print("g lik con close")


    def __get_dizlikes(self, user_id):
        self.__DB_connect()
        try:
            id_search_query = f"SELECT dizlikes FROM vk_bot_users WHERE user_id = {user_id}"
            self.cursor.execute(id_search_query)
            res = self.cursor.fetchone()
            return res
        finally:
            self.db_con.close()
            print("g lik con close")


    def update_likes(self, user_id):
        self.__DB_connect()
        try:
            res = self.__get_likes(user_id)
            res += 1
            update_query = f"UPDATE vk_bot_users SET likes = {res} WHERE user_id = {user_id}"
            self.cursor.execute(update_query)
            self.db_con.commit()
            self.cursor.close()
            del res
        finally:
            self.db_con.close()
            print("u lik con close")


    def update_dizlikes(self, user_id):
        self.__DB_connect()
        try:
            res = self.__get_dizlikes(user_id)
            res += 1
            update_query = f"UPDATE vk_bot_users SET likes = {res} WHERE user_id = {user_id}"
            self.cursor.execute(update_query)
            self.db_con.commit()
            self.cursor.close()
            del res
        finally:
            self.db_con.close()
            print("u dlik con close")

    # def __update_data(self, user_id, grade_mode):
    #     self.__DB_connect()
    #     try:
    #         if grade_mode == "LIKE":
    #             self.__update_likes(user_id)
    #         elif grade_mode == "DIZ":
    #             self.__update_dizlikes(user_id)
    #         print("dt upt")
    #         self.db_con.commit()
    #         self.cursor.close()

    #     finally:
    #         self.db_con.close()
    #         print("upd dt con close")

    

    def insert_data(self, user_id, likes=0, dizlikes=0):
        self.__DB_connect()
        try:
            if self.__id_exist(user_id):
                pass
            else:
                insert_query = "INSERT INTO vk_bot_users (user_id, likes, dizlikes) VALUES (%s, %s, %s)"
                self.cursor.execute(insert_query, user_id, likes, dizlikes)
                self.db_con.commit()
                self.cursor.close()
                print("dt ins ok")
        
        finally:
            self.db_con.close()
            print("dt ins con close") 


    