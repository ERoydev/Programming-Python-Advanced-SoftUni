


def shop_from_grocery_list(budget, grocery_list, *args):
    for name,price in args:
        if name in grocery_list:
            if budget < price:
                break

            grocery_list.remove(name)
            budget -= price

    if grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

    return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))