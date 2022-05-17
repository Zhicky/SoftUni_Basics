projection = input()
row = int(input())
column = int(input())
income = 0
cinema_capacity = row * column
if projection == 'Premiere':
    income = cinema_capacity * 12
elif projection == 'Normal':
    income = cinema_capacity * 7.50
elif projection == 'Discount':
    income = cinema_capacity * 5.00
print(f'{income:.2f}')