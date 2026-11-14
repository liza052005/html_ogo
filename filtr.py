import json
with open("products.json", "r", encoding="utf-8")as f:
    products = json.load(f)

    filtered_products = []
    for product in products:
        if product["price"] < 10000 and product["rating"]> 4.0:
            filtered_products.append(product)

    print(f"Найдено товаров: {len(filtered_products)}")
    print(filtered_products)