import json

with open("translator.json", "r") as my_file:
    orders = json.load(my_file)
print(f'{orders}')



max_price = 0
max_order = ''
# цикл по заказам                          1.Какой номер самого дорого заказа за июль?
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if orders_data['date'] <= '2023-31-07' and orders_data['date'] >= '2023-01-07':
        if price > max_price:
            max_order = order_num
            max_price = price

print(f'1.Номер самого дорогого заказа за июль: {max_order}, стоимость заказа: {max_price}')


max_quantity = 0
max_order = ''
# цикл по заказам                          2.Какой номер заказа с самым большим количеством товаров?
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'2.Номер заказа с самым большим количеством товаров: {max_order}, количество товаров: {max_quantity}')



max_quantity = 0
max_order = ''
date = 0
date_dict = {}

# цикл по заказам                          3.В какой день в июле было сделано больше всего заказов?
for order_num, orders_data in orders.items():
    # получаем
    date = orders_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1


for date in sorted(date_dict):
    max_value = max(date_dict.values())
    if date_dict[date] == max_value:
        print(f'3.Больше всего заказов в июле сделано: {date}, количество заказов: {date_dict[date]}')



max_orders = 0
max_order = ''
max_id = 0
user_dict = {}
# цикл по заказам                          4.Какой пользователь сделал самое большое количество заказов за июль?
for order_num, orders_data in orders.items():
    # получаем id пользователя
    user_id = orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + 1
    orders_id = user_dict.get(user_id)
    #
    if orders_id > max_orders:
        max_orders = orders_id

print(f'4.Id пользователя с самым большим количеством заказов за июль: {user_id}, количество заказов: {max_orders}')



sum_all = 0
count = 0
max_orders = 0
#max_order = ''
max_id = 0
user_dict = {}
# цикл по заказам _________________5.У какого пользователя самая большая суммарная стоимость заказов за июль?
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    user_id = orders_data['user_id']
    price = orders_data['price']

    user_dict[user_id] = user_dict.get(user_id, 0) + price
    orders_id = user_dict.get(user_id)
    if orders_id >= max_orders:
        max_orders = orders_id
        max_id = user_id
print(f'5.Id пользователя с самой большой суммарной стоимостью заказов за июль: {max_id}, суммарная стоимость заказов: {max_orders}')


sum_price = 0
sum_zak = 0
price = 0
date_dict = {}

# цикл по заказам                          6. Какая средняя стоимость заказа была в июле?
for order_num, orders_data in orders.items():
    # получаем
    price = orders_data['price']
    date = orders_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1
    sum_price += price

for date in sorted(date_dict):
    sum_zak += date_dict[date]

print(f'6.Cредняя стоимость заказа в июле составила: {sum_price/sum_zak}')


sum_price = 0
sum_quantity = 0
price = 0
quantity = 0
date_dict = {}

# цикл по заказам                          7/Какая средняя стоимость товаров в июле?
for order_num, orders_data in orders.items():
    # получаем
    price = orders_data['price']
    quantity = orders_data['quantity']
    sum_price += price
    sum_quantity += quantity

print(f'7.Cредняя стоимость товаров в июле составила: {sum_price/sum_quantity:.6}')





