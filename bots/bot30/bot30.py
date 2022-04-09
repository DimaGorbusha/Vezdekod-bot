import vk_api
from random import randint
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

meme_photos = [

] # Общий массив ссылок на мемы

liked_meme_photos = [

] # Массив лайкнутых ссылок на мемы

def meme_number_identification(): # Рандомно определяем номер мема
    global meme_photos, liked_meme_photos
    num = randint(0, 49)
    res = meme_photos[num]
    if res in liked_meme_photos:
        return meme_number_identification()
    return res

def main(): # Основноой скрипт
    global meme_photos, liked_meme_photos
    vk_session = vk_api.VkApi(token = "18d33784d350ef54c52974d857e065eecffdd08f2a62a3fc7675b5b788028665ce691e65ac52b19a8d816", api_version="5.131")
    vk_bot_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)    
    
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                vk_bot_api.messages.send(user_id = id,
                message='Лови мем',
                attachment="photo-212547636_457239017",
                random_id=get_random_id())


print(meme_number_identification())