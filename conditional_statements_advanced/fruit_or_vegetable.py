product = input()
fruit = product == "banana" or product == "apple" or product == "kiwi" or product == "lemon" or product == "grapes" or product == "cherry"
vegetable = product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot"


if fruit:
    print('fruit')
elif vegetable:
    print('vegetable')
else:
    print('unknown')