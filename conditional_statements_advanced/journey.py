budget = float(input())
season = input()
destination = ''
kind = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        kind = 'Camp'
        price = budget * 0.30
    else:
        kind = 'Hotel'
        price = budget * 0.7
if 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        kind = 'Camp'
        price = budget * 0.4
    else:
        kind = 'Hotel'
        price = budget * 0.8
if budget > 1000:
    destination = 'Europe'
    kind = 'Hotel'
    price = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{kind} - {price:.2f}')
