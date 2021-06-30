# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
for item in items:
    print(item["brand"], end=" ")
print()
# TODO: your code here
lst = []
for item in items:
    lst.append(item["brand"])

# print(lst)
col = {}

# print(lst.count("reebok"))
for item in items:
    col[item["brand"]] = lst.count(item["brand"])

vsego = 0
for item, sum in col.items():
    # print(item,sum)
    if sum > vsego:
        vsego = sum

# print(col)
print("На складе больше всего товаров брэнда(ов): ")
for item, sum in col.items():
    if sum == vsego:
        print(item, sum)

# TODO: your code here
price_max = 0
for item in items:
    if item.get("price") >  price_max:
        price_max = item.get("price")

#    print(item.get("brand"),item.get("price") )


print("На складе самый дорогой товар брэнда(ов): ")

for item in items:
    if item.get("price") == price_max:
        print(item.get("brand"))

