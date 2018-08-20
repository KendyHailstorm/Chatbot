from telegram.ext import Updater
token='610745320:AAEgL85_Ggl0qVJip-plTt880cw5i1TaJuM'

import requests
import datetime
import json
import requests
import time
import urllib

TOKEN = token
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_json_from_url(url):
    #content = get_telegram_url(url)
    response = requests.get(url)
    content = response.content.decode("utf8")
    js = json.loads(content)
    return js


def get_telegram_update(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:

        last_chat_text = (update["message"]["text"]);
        last_chat_name = update['message']['chat']['first_name'];
        last_chat_id = update["message"]["chat"]["id"];
        greetings = ('hello', 'hi', 'greetings', 'sup')
        now = datetime.datetime.now()
        new_offset = None
        today = now.day
        hour = now.hour
        print(last_chat_text)
        print(last_chat_name)

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            text =  'Good Morning  {}'.format(last_chat_name);
            send_telegram_message(text, last_chat_id)
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            text = 'Good Afternoon {}'.format(last_chat_name);
            send_telegram_message(text, last_chat_id)
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            text = 'Good Evening  {}'.format(last_chat_name);
            send_telegram_message(text, last_chat_id)
            today += 1


        text = "this is a telegram bot - replying back to your message: " + update["message"]["text"]
        print(text)
        chat = update["message"]["chat"]["id"]
        print(chat)
        send_telegram_message(text, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_telegram_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    #get_telegram_url(url)
    response = requests.get(url)
    content = response.content.decode("utf8")


def main():
    last_update_id = None
    print(URL);

    while True:
        updates = get_telegram_update(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
    time.sleep(0.5)


greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()

if __name__ == '__main__':
    main()
