count_pages = int(input())
pages_per_hour = int(input())
count_days = int(input())

total_time = count_pages / pages_per_hour
result = total_time / count_days
print(result)