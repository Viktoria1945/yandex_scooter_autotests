# Виктория Мотина, 48-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data


# Тест 1: Создание заказа
def test_create_order():
    response = sender_stand_request.post_new_order(data.order_body)
    assert response.status_code == 201


# Тест 2: Получение заказа по треку
def test_get_order_by_track():
    # Сначала создаём заказ, чтобы получить трек
    response_create = sender_stand_request.post_new_order(data.order_body)
    track = response_create.json()["track"]

    # Получаем заказ по треку
    response_get = sender_stand_request.get_order_by_track(track)
    assert response_get.status_code == 200