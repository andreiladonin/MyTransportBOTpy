import time
import requests
import json
from requests.sessions import Session
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


HEADERS = {
    "User-Agent": UserAgent().chrome
}

URL = "https://yandex.ru/maps/51/samara/stops/stop__10001875/?ll=50.276069%2C53.217901&tab=overview&z=14"

numbers_bus = ['480', '27', '75', '217']

def get_respone(url):
    sess = Session()

    r = sess.get(url, headers=HEADERS)
    time.sleep(2)
    soup = BeautifulSoup(r.text, "html.parser")

    content = soup.find('script', {"class" : 'config-view'}).contents

    data = json.loads(content[0]) 

    return data


def get_timing():

    data = False
    while True:
        data = get_respone(URL)
        if 'masstransitStop' in data:
            data = data["masstransitStop"]
            break

    s = "🚍 Остановка " + data['name'] + '\n'
    i = 0

    for transport in data['transports']:
        if transport["name"] in numbers_bus:
            """ print("Автобус №" + transport["name"]) """
            s += "Автобус 🚍 №" + transport["name"] + '\n'

            for thread in transport["threads"]:
                for event in thread['BriefSchedule']['Events']:
                    if 'Scheduled' in event and i ==0:
                        """ print('По расписанию ' + event['Scheduled']['text']) """
                        s += 'По расписанию ' + event['Scheduled']['text'] + '\n'
                        i=+1
                    if 'Estimated' in event:
                            """ print('Точное время прибытия ' + event['Estimated']['text']) """
                            s += 'Точное время прибытия ⌛' + event['Estimated']['text'] + '\n'
                i = 0
    
    return s
