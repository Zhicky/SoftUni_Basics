month = input()
nights_count = int(input())
room_type = ''
price_studio = 0
price_apartment = 0
if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
elif month == 'July' or month == "August":
    price_studio = 76
    price_apartment = 77
total_price_studio = price_studio * nights_count
total_price_apartment = price_apartment * nights_count
if nights_count > 14 and (month == 'May' or month == 'October'):
    total_price_studio -= total_price_studio * 0.3
elif nights_count > 7 and (month == 'May' or month == 'October'):
    total_price_studio -= total_price_studio * 0.05

if nights_count > 14 and (month == 'June' or month == 'September'):
    total_price_studio -= total_price_studio * 0.2
if nights_count > 14:
    total_price_apartment -= total_price_apartment * 0.1
print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')