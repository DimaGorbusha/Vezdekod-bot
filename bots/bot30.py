import vk_api
from random import randint
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from db.data_base import DB



# ---------Массивы---------
meme_photos = [ # Общий массив ссылок на мемы
    "photo-212547636_457239017", "photo-212547636_457239018", "photo-212547636_457239019", "photo-212547636_457239020", "photo-212547636_457239021", "photo-212547636_457239022", "photo-212547636_457239023", "photo-212547636_457239024", "photo-212547636_457239025", "photo-212547636_457239026", "photo-212547636_457239027", "photo-212547636_457239028", "photo-212547636_457239029", "photo-212547636_457239030", "photo-212547636_457239031","photo-212547636_457239032", "photo-212547636_457239033", "photo-212547636_457239034", "photo-212547636_457239035", "photo-212547636_457239036", "photo-212547636_457239037", "photo-212547636_457239038", "photo-212547636_457239039", "photo-212547636_457239040", "photo-212547636_457239041", "photo-212547636_457239042", "photo-212547636_457239043", "photo-212547636_457239044", "photo-212547636_457239045", "photo-212547636_457239046", "photo-212547636_457239047", "photo-212547636_457239048", "photo-212547636_457239049", "photo-212547636_457239050", "photo-212547636_457239051", "photo-212547636_457239052", "photo-212547636_457239053", "photo-212547636_457239054", "photo-212547636_457239055", "photo-212547636_457239056", "photo-212547636_457239057", "photo-212547636_457239058", "photo-212547636_457239059", "photo-212547636_457239060", "photo-212547636_457239061", "photo-212547636_457239062", "photo-212547636_457239063", "photo-212547636_457239064", "photo-212547636_457239065", "photo-212547636_457239066"] 

liked_meme_photos = [

] # Массив лайкнутых ссылок на мемы

meme_grade_flag = False


# ---------Клавиатуры---------
keyboard_mem = VkKeyboard(one_time=False)

# ----Кнопки----
keyboard_mem.add_button('Мем', color=VkKeyboardColor.SECONDARY)
keyboard_mem.add_line()
keyboard_mem.add_button('Статистика', color=VkKeyboardColor.PRIMARY)
keyboard_mem.add_line()
keyboard_mem.add_button('Лайк', color=VkKeyboardColor.POSITIVE)
keyboard_mem.add_button('Дизлайк', color=VkKeyboardColor.NEGATIVE)

# ---------Основной код----------
def meme_number_identification(): # Определяем мем
    global meme_photos, liked_meme_photos
    num = randint(0, 49)
    res = meme_photos[num]
    if res in liked_meme_photos:
        return meme_number_identification()
    return res


def main(): # Основной скрипт
        global meme_photos, liked_meme_photos, meme_grade_flag
        vk_session = vk_api.VkApi(token = "18d33784d350ef54c52974d857e065eecffdd08f2a62a3fc7675b5b788028665ce691e65ac52b19a8d816", api_version="5.131")
        vk_bot_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)

        data_base = DB()    
        
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    message = event.text.lower()
                    id = event.user_id
                    if message == 'мем' or message == 'мемес' or message == 'мемас' or message == 'мемчанский':
                        meme_grade_flag = True
                        mem_num = meme_number_identification()
                        vk_bot_api.messages.send(peer_id = id,
                        message='Лови мем',
                        attachment=mem_num,
                        keyboard=keyboard_mem.get_keyboard(),
                        random_id=get_random_id())

                    message = event.text.lower()
                    id = event.user_id
                    if message == 'лайк' and meme_grade_flag:
                        liked_meme_photos.append(mem_num)
                        data_base.update_likes(id)
                        meme_grade_flag = False


                    if message == 'дизлайк' and meme_grade_flag:
                        liked_meme_photos.append(mem_num)
                        data_base.update_dizlikes(id)
                        meme_grade_flag = False

                    if message == 'статистика':
                        likes_us_tuple = data_base.get_likes_user(id)
                        stat_us_likes = likes_us_tuple[0]
                        dizlikes_us_tuple = data_base.get_dizlikes_user(id)
                        stat_us_dizlikes = dizlikes_us_tuple[0]

                        likes_all_tuple = data_base.get_likes_all()
                        likes_all_stat = likes_all_tuple[0]
                        dizlikes_all_tuple = data_base.get_dizlikes_all()
                        dizlikes_all_stat = dizlikes_all_tuple[0]

                        stat = f"""Статистика:
                        Твои лайки: {stat_us_likes} 👍🏻
                        Твои дизлайки: {stat_us_dizlikes} 👎🏻
                        Общее количество лайков: {likes_all_stat}
                        Общее количество дизлайков: {dizlikes_all_stat}
                        """
                        vk_bot_api.messages.send(peer_id = id,
                        message=stat,
                        random_id=get_random_id())

if __name__ == '__main__':
    main()