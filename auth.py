import json
import random

categories = ["Электроника", "Аксуссуары", "Книги",
               "Игрушки", "Одежда", "Обувь", "Спорт", "Красота"]

product_names = [
    "Наушники", "Телефон", "Планшет", "Клавиатура", "Мышь", "Монитор", "Колонка",
    "Чехол", "Зарядка", "Кабель", "Сумка", "Рюкзак", "Журнал", "Стекло",
    "Кукла", "Машинка", "Мяч", "Конструктор", "Джинсы", "Кофта", "Куртка", "Ролики",
    "Крем", "Шампунь", "Духи", "Велосипед", "Футболка", "Платье"
]
products = []
for i in range(1, 1001):
    product = {
        "id": i,
        "name": f"{random.choice(product_names)} {random.randint(1, 100)}",
        "price": round(random.uniform(50, 50000), 2),
        "rating": round(random.uniform(1.0, 5.0), 1),
        "category": random.choice(categories),
        "in_stock": random.choice([True, False])
    }
    products.append(product)
with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=4)
print("Файл готов, количество товаров: ", len(products))