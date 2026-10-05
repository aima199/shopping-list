shopping_list = [
    {"item": "Milk", "price": 2.50, "purchased": True},
    {"item": "Bread", "price": 1.50, "purchased": False},
    {"item": "Eggs", "price": 3.00, "purchased": True},
    {"item": "Apples", "price": 4.00, "purchased": False}
]

print(shopping_list)

unpurchased = [item for item in shopping_list if not item["purchased"]]

print("Unpurchased items:")
for item in unpurchased:
    print(item["item"])