import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def main():
	vk_bot = vk_api.VkApi(token = "18d33784d350ef54c52974d857e065eecffdd08f2a62a3fc7675b5b788028665ce691e65ac52b19a8d816")
	vk_bot_api = vk_bot.get_api()
	longpoll = VkLongPoll(vk_bot)

	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			if event.to_me:
				message = event.text.lower()
				id = event.user_id
      
				if message == 'привет':
					vk_bot_api.messages.send(user_id = id, message='Привет вездекодерам!', random_id=0)
   

if __name__ == '__main__':
    main()