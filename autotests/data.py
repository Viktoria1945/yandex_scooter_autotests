# Заголовки для HTTP-запроса
headers = {
    "Content-Type": "application/json"
}

# Тело запроса для создания заказа
order_body = {
    "firstName": "Виктория",
    "lastName": "Мотина",
    "address": "ул. Ленина, д. 1",
    "metroStation": 4,
    "phone": "+79995553322",
    "rentTime": 3,
    "deliveryDate": "2026-10-15",
    "comment": "Тест",
    "color": ["BLACK"]
}