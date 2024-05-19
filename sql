Last login: Sun May 19 12:37:39 on ttys000
valeria@MacBook-Pro-Valeria ~ % ssh 016242d4-22f2-4a4a-b4c9-238914ce78cc@serverhub.praktikum-services.ru -p 4554
morty@4822392b6773:~$ psql -U morty -d scooter_rent
Password for user morty: 
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.

scooter_rent=# SELECT c.login, COUNT(o.id) AS orders_in_delivery
scooter_rent-# FROM "Couriers" c
scooter_rent-# JOIN "Orders" o ON c.id = o."courierId"
scooter_rent-# WHERE o."inDelivery" = true
scooter_rent-# GROUP BY c.login;
 login | orders_in_delivery 
-------+--------------------
(0 rows)

scooter_rent=# SELECT o.track,
scooter_rent-#     CASE
scooter_rent-#         WHEN o.finished = true THEN 2
scooter_rent-#         WHEN o.cancelled = true THEN -1
scooter_rent-#         WHEN o."inDelivery" = true THEN 1
scooter_rent-#         ELSE 0
scooter_rent-#     END AS status
scooter_rent-# FROM "Orders" o;
 track | status 
-------+--------
(0 rows)

scooter_rent=#
