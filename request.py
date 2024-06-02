# Лера Абрамс, 16-я когорта — Финальный проект. Инженер по тестированию плюс

import requests


URL_TEMPLATE = 'https://b60b8f10-6b6e-49a4-9210-b8758a409fd1.serverhub.praktikum-services.ru/api/v1/orders'
PARAM_JSON = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}


def get_track_num():
    place_order_request = requests.post(URL_TEMPLATE, json=PARAM_JSON)
    return place_order_request.json()['track']


def get_status_code(track_num):
    new_url = URL_TEMPLATE + '/track?t=' + str(track_num)
    get_order_by_tracknum_request = requests.get(new_url)
    return get_order_by_tracknum_request.status_code


def run_test():
    track_num = get_track_num()
    return get_status_code(track_num)


assert run_test() == 200

print('Well done! Status code 200 returned')



