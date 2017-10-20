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
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        if text == "січень":
            send_message("Цикорій, савойська капуста, червона капуста, брюссельська капуста, білокачанна капуста, цибуля-шалот, цибуля-порей, ріпа, артишок, пастернак, грейпфрут, лимон, апельсин, мандарин, груша, айва, хурма, гливи", chat)
        elif text == "лютий":
            send_message("Цикорій, червона капуста, брюссельська капуста, білокачанна капуста, цибуля-шалот, пастернак, грейпфрут, лимон, апельсин, мандарин, гливи", chat)
        elif text == "березень":
            send_message("Гливи", chat)
        elif text == "квітень":
            send_message("Спаржа, шпинат, ревінь, редька", chat)
        elif text == "травень":
            send_message("Спаржа, качановий салат, латук, молодий горошок, редис, рукола, шпинат, бруква, редька, капуста білокачанна, крес водяний, опеньки, зелена цибуля, м\"ята", chat)
        elif text == "червень":
            send_message("Спаржа, квасоля, молодий кабачок, зелений горошок, солодкий перець, брокколі, морква, кольорова капуста, огірок, качановий салат, латук, редис, крес водяний, шпинат, бруква, редька, полуниця, вишня, агрус, червона смородина, суниця, черешня, чорниця, бузина, м\"ята, щавель, зелена цибуля, опеньки, кріп, петрушка, лисички", chat)
        elif text == "липень":
            send_message("Баклажан, цвітна капуста, огірок, фенхель, крес водяний, зелений горошок, кабачок, молода картопля, помідор, квасоля, болгарський перець, брокколі, морква, кольорова капуста, селера, качановий салат, цибуля-порей, латук, цибуля ріпчаста, горох, редис, червона капуста, листяний салат, редька, полуниця, абрикос, персик, малина, нектарин, агрус, вишня, черешня, чорна смородина, порічка, чорниця, шавлія, щавель, кріп, петрушка, зелений лук, м\"ята, опеньки, білий гриб, підосиновики, лисички", chat)
        elif text == "серпень":
            send_message("Баклажан, болгарський перець, цукіні, фенхель, зелений горошок, брокколі, кукурудза, картопля, помідор, огірок, морква, кольорова капуста, савойська капуста, селера, кабачок, горох, цибуля ріпчаста, редис, червона капуста, листовий салат, бруква, листовий буряк, редька, кавун, диня, слива, агрус, персик, нектарин, абрикос, чорниця, базилік, щавель, зелена цибуля, м\"ята, опеньки, білий гриб, підосиновики, лисички", chat)
        elif text == "вересень":
            send_message("Огірок, баклажан, болгарський перець, брокколі, морква, кольорова капуста, селера, кабачок, фенхель, хрін, цибуля-порей, цибуля ріпчаста, гарбуз, редис, помідор, капуста, бруква, яблуко, слива, груша, інжир, диня, кавун, бузина, опеньки, лисички, білий гриб, підосиновики", chat)
        elif text == "жовтень":
            send_message("Брокколі, морква, кольорова капуста, селера, цикорій, кабачок, фенхель, хрін, салат рапунцель, цибуля порей, гарбуз, брюссельська капуста, помідор, бруква, ріпа, яблуко, бузина, інжир, груша, лисички", chat)
        elif text == "листопад":
            send_message("Морква, кольорова капуста, цикорій, пастернак, хрін, салат рапунцель, цибуля-порей, гарбуз, савойська капуста, брюссельська капуста, ріпа, журавлина, груша, айва, хурма, гливи", chat)
        elif text == "грудень":
            send_message("Цикорій, брюссельська капуста, селера, пастернак, гарбуз, ріпа, цибуля-порей, журавлина, мандарин, груша, гранат, апельсин, грейпфрут, айва, хурма, гливи", chat)
        elif text == "/start":
            send_message_hello(chat)
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


def send_message_hello(chat_id):
    #video = urllib.parse.quote(video)
    url = URL + "sendVideo?chat_id={}&video=https://media.giphy.com/media/3o7bueCmD3eTtGvb0c/giphy.gif".format(chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == "__main__":
    main()