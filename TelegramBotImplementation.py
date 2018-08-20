from telegram.ext import Updater
import requests
import datetime
import json
import requests
import time
import urllib
import sys

token='610745320:AAEgL85_Ggl0qVJip-plTt880cw5i1TaJuM'

TOKEN = token
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


    #######
    # program to extract weather details
def get_last_chat_message(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (chat_id)


api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=ae981acaacc4759d8a0f0e7cd5a37e42&q='
#city = input('City Name :')
city = get_last_chat_message()
url = str(api_address) + str(city)
json_data = requests.get(url).json()
description_of_Weather_main = json_data['weather'][0]['main'] #Get the weather of the city from the json
description_of_Weather = json_data['weather'][0]['description']
description_of_Weather_name = json_data['name']
description_of_Weather_temperature = json_data['main']['temp']
celsius = description_of_Weather_temperature - 273

    #######




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



        text = "this is a telegram bot - replying back to your message: " + update["message"]["text"]
        print(text)
        chat = update["message"]["chat"]["id"]
        print(chat)
        send_telegram_message(description_of_Weather_main, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_telegram_message(description_of_Weather_main, chat_id):
    #text = urllib.parse.quote_plus(text)
    #url = URL + "sendMessage?text={}&chat_id={}".format(description_of_Weather_main, chat_id)
    



    #get_telegram_url(url)
    url = URL + "sendMessage?text={}&chat_id={}".format(description_of_Weather_main, chat_id)
    response = requests.get(url)
    content = response.content.decode("utf8")


def main():
    last_update_id = None
    print(URL)

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
