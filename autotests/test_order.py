# Виктория Мотина, 48-я когорта — Финальный проект. Инженер по тестированию плюс

# Импорт необходимых модулей
import sender_stand_request
import data


# Тест: создание заказа и получение его по треку
def test_create_and_get_order():
    # Создаём заказ
    response = sender_stand_request.post_new_order(data.order_body)
    
    # Проверяем, что заказ создан (код 201)
    assert response.status_code == 201
    
    # Сохраняем трек заказа
    track = response.json()["track"]
    
    # Получаем заказ по треку
    response_get = sender_stand_request.get_order_by_track(track)
    
    # Проверяем, что код ответа равен 200
    assert response_get.status_code == 200