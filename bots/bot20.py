import vk_api
from vk_api.utils import get_random_id
import json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# -------Creating Keyboards-------
simple_keyboard1_greet = VkKeyboard(one_time=True)
simple_keyboard2_loc = VkKeyboard(one_time=True)
simple_keyboard3_donate = VkKeyboard(one_time=True)
inline_keyboard4_like = VkKeyboard(one_time=False, inline=True)
simple_keyboard5_weather = VkKeyboard(one_time=True)
inline_keyboard6_link = VkKeyboard(one_time=False, inline=True)
simple_keyboard7_vezdekod = VkKeyboard(one_time=True)
inline_keyboard8_poll = VkKeyboard(one_time=False, inline=True)

simple_keyboard1_greet.add_button('Да, где-то точно виделись', color=VkKeyboardColor.PRIMARY)
simple_keyboard1_greet.add_line()
simple_keyboard1_greet.add_button('Нет, впервые вижу', color=VkKeyboardColor.SECONDARY)

simple_keyboard2_loc.add_location_button()

simple_keyboard3_donate.add_vkpay_button(hash="action=transfer-to-group&group_id=74030368&aid=6222115")

inline_keyboard4_like.add_callback_button(
        label="Нравится :)",
        color=VkKeyboardColor.POSITIVE,
        payload={"type": "show_snackbar", "text": "Спасибо <3"},
    )

inline_keyboard4_like.add_callback_button(
        label="Не нравится ;(",
        color=VkKeyboardColor.NEGATIVE,
        payload={
			"type": "show_snackbar",
			"text": "Спасибо! Мы обязательно станем лучше!"},
    )

simple_keyboard5_weather.add_button('Ясно', color=VkKeyboardColor.POSITIVE)
simple_keyboard5_weather.add_line()
simple_keyboard5_weather.add_button('Пасмурно', color=VkKeyboardColor.NEGATIVE)
simple_keyboard5_weather.add_line()
simple_keyboard5_weather.add_button('Ливень', color=VkKeyboardColor.PRIMARY)
simple_keyboard5_weather.add_button('Туман', color=VkKeyboardColor.SECONDARY)

inline_keyboard6_link.add_openlink_button(label='Наше сообщество', link='https://vk.com/vezdekoders')

simple_keyboard7_vezdekod.add_vkapps_button(
	app_id=6979558, 
    owner_id=-181108510, 
    label="Вездекод",
    hash="sendKeyboard"
)
inline_keyboard8_poll.add_button('Очень!', color=VkKeyboardColor.POSITIVE)
inline_keyboard8_poll.add_button('Не совсем :(', color=VkKeyboardColor.NEGATIVE)
inline_keyboard8_poll.add_line()
inline_keyboard8_poll.add_vkpay_button(hash="action=transfer-to-group&group_id=74030368&aid=6222115")


# ------------Main code---------------
def main():
	vk_session = vk_api.VkApi(token = "18d33784d350ef54c52974d857e065eecffdd08f2a62a3fc7675b5b788028665ce691e65ac52b19a8d816", api_version="5.131")
	vk_bot_api = vk_session.get_api()
	longpoll = VkLongPoll(vk_session)

	for event in longpoll.listen():
		if event.to_me and event.type == VkEventType.MESSAGE_NEW:
			if event.text != "":
				id = event.user_id

				vk_bot_api.messages.send(
					user_id=id,
					random_id=get_random_id(),
					peer_id=id,
					keyboard=simple_keyboard1_greet.get_keyboard(),
					message="Здравствуйте! Мы знакомы?)",
				)
		
		if event.to_me and event.type == VkEventType.MESSAGE_NEW:
			if event.text != "":
				id = event.user_id

				vk_bot_api.messages.send(
                    user_id=id,
                    random_id=get_random_id(),
                	peer_id=id,
                    keyboard=simple_keyboard2_loc.get_keyboard(),
                    message="Где вы живёте?",
                )
		
		if event.to_me and event.type == VkEventType.MESSAGE_NEW:
			if event.text != "":
				id = event.user_id

				vk_bot_api.messages.send(
                    user_id=id,
                    random_id=get_random_id(),
                	peer_id=id,
                    keyboard=simple_keyboard3_donate.get_keyboard(),
                    message="Наше сообщество активно развивается! Хотите ли вы нас поддержать?)",
                )

		if event.to_me and event.type == VkEventType.MESSAGE_NEW:
			if event.text != "":
				id = event.user_id

				vk_bot_api.messages.send(
                    user_id=id,
                    random_id=get_random_id(),
                	peer_id=id,
                    keyboard=inline_keyboard4_like.get_keyboard(),
                    message="Вам нравится наш бот?",
                )		

		if event.to_me and event.type == VkEventType.MESSAGE_NEW:
			if event.text != "":
				id = event.user_id

				vk_bot_api.messages.send(
					user_id=id,
					random_id=get_random_id(),
					peer_id=id,
					keyboard=simple_keyboard5_weather.get_keyboard(),
					message="Какая у вас погода?",
				)

		if event.to_me and event.type == VkEventType.MESSAGE_NEW:
			if event.text != "":
				id = event.user_id

				vk_bot_api.messages.send(
					user_id=id,
					random_id=get_random_id(),
					peer_id=id,
					keyboard=inline_keyboard6_link.get_keyboard(),
					message="Вы уже были у нас в сообществе?",
				)

		if event.to_me and event.type == VkEventType.MESSAGE_NEW:
			if event.text != "":
				id = event.user_id

				vk_bot_api.messages.send(
					user_id=id,
					random_id=get_random_id(),
					peer_id=id,
					keyboard=simple_keyboard7_vezdekod.get_keyboard(),
					message="А вы участвуете в хакатоне Вездкод?",
				)

		if event.to_me and event.type == VkEventType.MESSAGE_NEW:
			if event.text != "":
				id = event.user_id

				vk_bot_api.messages.send(
					user_id=id,
					random_id=get_random_id(),
					peer_id=id,
					keyboard=inline_keyboard8_poll.get_keyboard(),
					message="Вам понравились наши вопросы?",
				)

if __name__ == '__main__':
	main()