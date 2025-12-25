import requests
import time
import random
# Импортируем переменные из твоего конфига
from config.vk_config import VK_ACCESS_TOKEN, VK_GROUP_ID, VK_API_VERSION

class VKBot:
    def __init__(self):
        self.token = VK_ACCESS_TOKEN
        self.group_id = VK_GROUP_ID
        self.version = VK_API_VERSION
        self.api_url = "https://api.vk.com/method/"
        
        # Параметры LongPoll
        self.server = None
        self.key = None
        self.ts = None

    def _get_longpoll_params(self):
        """Получаем данные для подключения к серверу VK"""
        params = {
            'group_id': self.group_id,
            'access_token': self.token,
            'v': self.version
        }
        try:
            response = requests.get(f"{self.api_url}groups.getLongPollServer", params=params).json()
            if 'error' in response:
                print(f"[!] Ошибка API: {response['error']['error_msg']}")
                return False
            
            res = response['response']
            self.server = res['server']
            self.key = res['key']
            self.ts = res['ts']
            return True
        except Exception as e:
            print(f"[!] Не удалось связаться с VK: {e}")
            return False

    def send_message(self, peer_id, text):
        """Функция отправки сообщения"""
        params = {
            'peer_id': peer_id,
            'message': text,
            'random_id': random.randint(1, 1000000),
            'access_token': self.token,
            'v': self.version
        }
        requests.post(f"{self.api_url}messages.send", data=params)

    def listen(self):
        """Основной цикл прослушивания"""
        if not self._get_longpoll_params():
            print("Критическая ошибка при запуске. Проверь токен в .env")
            return

        print("--- БОТ УСПЕШНО ЗАПУЩЕН ---")
        
        while True:
            try:
                # Ожидаем события от VK
                lp_params = {
                    'act': 'a_check',
                    'key': self.key,
                    'ts': self.ts,
                    'wait': 25
                }
                response = requests.get(self.server, params=lp_params, timeout=30).json()

                if 'failed' in response:
                    # Если сессия устарела — обновляем
                    self._get_longpoll_params()
                    continue

                self.ts = response['ts']

                for event in response.get('updates', []):
                    if event['type'] == 'message_new':
                        msg = event['object']['message']
                        user_id = msg['from_id']
                        text = msg['text'].lower()

                        print(f"Новое сообщение: {text} от {user_id}")

                        # ЛОГИКА ГАЙДА
                        if text == '/start':
                            self.send_message(user_id, "Привет! Чтобы получить гайд, просто напиши слово 'Гайд'.")
                        
                        elif 'гайд' in text:
                            # Вставь сюда ссылку на свой пост или статью
                            self.send_message(user_id, "Держи обещанный гайд по продвижению: [https://vk.com/market/product/kod-spokoystvia-praktiki-dlya-it-spetsialista-protiv-vygorania-i-trevozhnostiquot-pdf-232414007-13300604]")
                        
                        else:
                            self.send_message(user_id, "Я тебя услышал. Напиши 'Гайд', если хочешь обучение.")

            except Exception as e:
                print(f"Ошибка в цикле: {e}")
                time.sleep(5)
                self._get_longpoll_params()

if __name__ == "__main__":
    bot = VKBot()
    bot.listen()