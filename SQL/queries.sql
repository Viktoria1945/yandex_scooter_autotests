-- Задание 1: Логины курьеров с количеством заказов в статусе "В доставке"
SELECT "Couriers".login, COUNT("Orders".id) AS orders_count
FROM "Couriers"
JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;

-- Задание 2: Трекеры заказов и их статусы
SELECT "Orders".track,
       CASE
           WHEN "Orders".finished = true THEN 2
           WHEN "Orders".cancelled = true THEN -1
           WHEN "Orders"."inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders";