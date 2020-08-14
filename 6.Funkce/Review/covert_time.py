#!/usr/bin/env python3

time = input("Please enter your time: ")
time1 = time.split(':')
hour = 0
if int(time1[0]) > 11:
    hour = int(time1[0]) % 12
    print(str(hour) + ':' + time1[1] + 'PM')

else:
    print('Converted to English: ', time, 'AM')


hours, min = time.split(":")
print(hours)
print(min)

adjusted_h = hours if int(hours)==12 else str(int(hours) % 12)
daytime = ['AM', 'PM'][int(hours)>=12]
print(adjusted_h + ":" + min)
