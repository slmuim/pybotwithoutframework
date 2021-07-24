import requests
import random

BOT_TOKEN = '' #YOUR TOKEN FROM BOTFATHER
API_LINK = f'https://api.telegram.org/bot{BOT_TOKEN}/'


def getLastMessage():
    """Получение текста последнего полученного сообщения"""
    update = requests.get(API_LINK + 'getUpdates?offset=-1').json()
    message_text = update['result'][0]['message']['text']
    from_chat_id = update['result'][0]['message']['chat']['id']
    result = {'chat_id': from_chat_id, 'text': message_text}
    return result


def sendMessage():
    """Отправка эхо сообщения"""
    phrases = [
         'Много не шути даун',
         'Маме расскажу',
         'Язык вырву',
         'Драться будешь?',
         'Не болтай много',
         'Лее вацок на коленях буищ извиняться за слова такие',
         'Лошара тупая'
    ]
    request = getLastMessage()
    chat_id = request['chat_id']
    text = request['text']
    if text == '/start':
         text = 'Нет бл /stop'
    elif text == '/stop':
         text = 'Нет бл /start'
    elif 'лох' in text.lower():
         text = random.choice(phrases)
         print('Меня оскорбили 🥵')
    elif 'даун' in text.lower():
         text = random.choice(phrases)
         print('Меня оскорбили 🥵')
    elif 'дебил' in text.lower():
         text = random.choice(phrases)
         print('Меня оскорбили 🥵')
    elif 'хуй' in text.lower():
         text = random.choice(phrases)
         print('Меня оскорбили 🥵')
    elif 'нахуй' in text.lower():
         text = random.choice(phrases)
         print('Меня оскорбили 🥵')
    elif 'лошара' in text.lower():
         text = random.choice(phrases)
         print('Меня оскорбили 🥵')
    elif 'ебал' in text.lower():
         text = random.choice(phrases)
         print('Меня оскорбили 🥵')
    else:
         text = 'ок'
    requests.get(f'{API_LINK}sendMessage?chat_id={chat_id}&text={text}')

def monitoring():
    """Проверка обновлений"""
    print('Monitoring...')
    request = requests.get(API_LINK + 'getUpdates?offset=-1').json()
    current_message = request['result'][0]['update_id']
    while True:
         r = requests.get(API_LINK + 'getUpdates?offset=-1').json()
         u_id = r['result'][0]['update_id']
         if u_id == current_message:
              continue
         elif 'my_chat_member' in r['result'][0]:
             print('Один ливнул\n')
             current_message = requests.get(API_LINK + 'getUpdates?offset=-2').json()
             break
         else: 
             sendMessage()
             print('Message sent!\n')
             break

while True:
     monitoring()
