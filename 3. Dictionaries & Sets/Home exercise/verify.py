data = {'user1': 'password1', 'Marek': '1234', 'Danko': 'qwert'}

username = input('Please enter username: ')
passwd = input('Please enter password: ')

if data.get(username, None) == passwd:
    print("Permission continue, GRANTED!")
else:
    print("Password or username are WRONG!")


#print(data)
