purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

dict_len = len(purchases)
revenue = 0

for i in range(dict_len):
    quant = purchases[i]["quantity"]
    price = purchases[i]["price"]
    revenue += price * quant

print(f'Общая выручка: {revenue}')