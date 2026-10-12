# Импорт необходимых модулей
import requests
import configuration
import data


# Функция для создания нового заказа
def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.ORDERS_PATH,
        json=body,
        headers=data.headers
    )


# Функция для получения заказа по треку
def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.ORDERS_TRACK_PATH,
        params={"t": track}
    )