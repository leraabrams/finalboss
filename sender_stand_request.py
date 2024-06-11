# Лера Абрамс, 16-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
from configuration import URL_SERVICE, CREATE_ORDERS
import data


def create_order_and_get_track():
    response = requests.post(URL_SERVICE + CREATE_ORDERS, json=data.order_body)
    track_number = response.json()["track"]
    return track_number


def get_order_by_track(track):
    get_order_url = f"{URL_SERVICE}{CREATE_ORDERS}/track?t={track}"
    response = requests.get(get_order_url)
    return response



def test_order_creation_and_retrieval():
    track_number = create_order_and_get_track()
    response = get_order_by_track(track_number)

