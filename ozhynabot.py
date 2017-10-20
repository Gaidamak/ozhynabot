#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import json
import requests
import time
import urllib





TOKEN = "473588601:AAFxZPg3l_HcwESu72G2mAgYzIp9qmEqf8U"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
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
        text = update['message']['text']
        chat = update["message"]["chat"]["id"]
        if text == 'січень':
            send_message('```Цикорій '
                         'савойська капуста,'
                         'червона капуста,'
                         'брюссельська капуста,'
                         'білокачанна капуста, цибуля-шалот, цибуля-порей, ріпа, артишок, пастернак, грейпфрут, лимон, апельсин, мандарин, груша, айва, хурма, гливи```', chat)
        elif text == 'груша':
            send_document(chat)
        elif text == 'lisichki':
            send_document(chat)
        else:
            send_message(text, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote(text)
    url = URL + "sendMessage?text={}&parse_mode=Markdown&chat_id={}".format(text, chat_id)
    get_url(url)


def send_document(chat_id):
    #video = urllib.parse.quote(video)
    url = URL + "sendVideo?chat_id={}&video=https://media.giphy.com/media/ur6Eqdu0WIeiI/giphy.gif".format(chat_id)
    get_url(url)



def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()