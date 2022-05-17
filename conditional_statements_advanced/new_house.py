flower_kind = input()
flower_count = int(input())
budget = int(input())
final_price = 0
if flower_kind == 'Roses':
    if flower_count > 80:
        final_price = (flower_count * 5) * 0.90
    else:
        final_price = flower_count * 5
elif flower_kind == 'Dahlias':
    if flower_count > 90:
        final_price = (flower_count * 3.80) * 0.85
    else:
        final_price = flower_count * 3.80
elif flower_kind == 'Tulips':
    if flower_count > 80:
        final_price = (flower_count * 2.80) * 0.85
    else:
        final_price = flower_count * 2.80
elif flower_kind == 'Narcissus':
    if flower_count < 120:
        final_price = (flower_count * 3) + (flower_count * 0.45)
    else:
        final_price = flower_count * 3
elif flower_kind == 'Gladiolus':
    if flower_count < 80:
        final_price = (flower_count * 2.50) + (flower_count * 0.5)
    else:
        final_price = flower_count * 2.50
if budget >= final_price:
    print(f'Hey, you have a great garden with {flower_count} {flower_kind} and {budget - final_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {final_price - budget:.2f} leva more.')

