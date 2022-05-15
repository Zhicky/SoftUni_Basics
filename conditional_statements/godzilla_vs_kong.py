budget = float(input())
people_count = int(input())
wear_price = float(input())

if people_count > 150:
    wear_price = wear_price * 0.90
decor = budget * 0.10
wear_count = people_count * wear_price
if decor + wear_count > budget:
    print('Not enough money!')
    print(f'Wingard needs {(decor + wear_count) - budget:.2f} leva more.')
elif decor + wear_count <= budget:
    print("Action!")
    print(f'Wingard starts filming with {budget - (decor + wear_count):.2f} leva left.')