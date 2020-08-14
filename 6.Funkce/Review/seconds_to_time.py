#!/usr/bin/env python3

sec = int(input("Please enter the no. of seconds since midnight: "))

hours, remain_sec = divmod(sec, 3600)
minutes = remain_sec//60

if len(str(minutes)) == 1:
    minutes = '0' + str(minutes)

daytime = ['AM','PM'][hours>=12]

print(str(hours) + ':' + str(minutes) + daytime)



#### solution from website:
seconds = int(input('Please enter the no. of seconds since midnight: '))

hours, remain_seconds = divmod(seconds,3600)
adjusted_h = hours if hours==12 else hours% 12
minutes = remain_seconds // 60

if len(str(minutes)) == 1:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)

daytime = ['AM','PM'][hours>=12]

print("It's: " + str(adjusted_h) + ':' + minutes + " " + daytime)
