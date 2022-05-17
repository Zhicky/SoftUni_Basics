exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
diff = arrival_time - exam_time

state = ''
if diff < -30:
    state = 'Early'
elif diff <= 0:
    state = 'On time'
else:
    state = 'Late'

result = ''
if diff != 0:
    hours = abs(diff) // 60
    minutes = abs(diff) % 60

    if hours > 0:
        if diff < 0:
            result = f'{hours}:{minutes:02d} hours before the start'
        else:
            result = f'{hours}:{minutes:02d} hours after the start'
    else:
        if diff < 0:
            result = f'{minutes} minutes before the start'
        else:
            result = f'{minutes} minutes after the start'

print(f'{state}')
if diff != 0:
    print(f'{result}')