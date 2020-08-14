time = input('Please enter your time: ')

hours, minutes = time.split(':')

hours = int(hours)
if hours > 11:
    print("Converted to English: ", hours%12, ':', minutes, 'PM')

else:
    print("Converted to English: ", hours, ':', minutes, 'AM')



#################################
adjusted_hour = hours if int(hours)==12 else int(hours)%12
daytime = ['AM', 'PM'][int(hours)>=12]
print("Converted to English: " + str(adjusted_hour) + ":" + minutes + daytime)
