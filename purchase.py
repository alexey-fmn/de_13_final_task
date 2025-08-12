purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

categories = {}
max_price_value = 1.0
category_prices = {}
category_quantity = {}

revenue = sum(p["price"] * p["quantity"] for p in purchases)

for purchase in purchases:
    category = purchase["category"]
    item = purchase["item"]
    if category not in categories:
        categories[category] = []
    if item not in categories[category]:
        categories[category].append(item)

expensive_items = [p for p in purchases if p["price"] >= max_price_value]

for purchase in purchases:
    category = purchase["category"]
    price = purchase["price"]
    quantity = purchase["quantity"]

    if category not in category_prices:
        category_prices[category] = {"total_price": 0, "total_quantity": 0}

    category_prices[category]["total_price"] += quantity * price
    category_prices[category]["total_quantity"] += quantity

average_price = {
    category: round(data["total_price"] / data["total_quantity"], 2)
    for category, data in category_prices.items()
}

for purchase in purchases:
    category = purchase["category"]
    quantity = purchase["quantity"]
    if category not in category_quantity:
        category_quantity[category] = 0
    category_quantity[category] += quantity

most_frequent = max(category_quantity, key=category_quantity.get)

print(f'Общая выручка: {revenue}')
print(f'Товары по категориям: {categories}')
print(f'Покупки дороже {max_price_value}: {expensive_items}')
print(f'Средняя цена по категориям: {average_price}')
print(f'Категория с наибольшим количеством проданных товаров: {most_frequent}')
