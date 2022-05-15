record_per_seconds = float(input())
meters = float(input())
time_per_seconds = float(input())
total_time = meters * time_per_seconds
delay = meters // 15 * 12.5
total_time += delay
if total_time < record_per_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - record_per_seconds:.2f} seconds slower.')