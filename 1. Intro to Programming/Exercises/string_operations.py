#Create script, which will:
#request a name from a user and store it in the variable name,
#print variable name,
#request a surname from a user and save it to variable surname,
#print variable surname,
#create variable full_name, in which you save the concatenation of name andsurname,
#print variable name_length, which will contain the length of full name
#print variable full_name, which will be bounded by rows of equal signs from both the top and the bottom. To do this, use the repeat operation, using = as many times as many characters are contained in full_name


# Save name
name = input("Add your name: ")

# Print name
print('Saving \'' + name + '\' into name...')

# Save surname
surname = input("Add your surname: ")

# Print surname
print('Saving \'' + surname + '\' into surname...')


# Create and print variable full_name
full_name = name + ' ' + surname
print('Full name:', full_name)


# Create and print variable name_length
name_length = len(full_name)
print('Lenghtof full name:',name_length)

# Print bounded variable full_name
print('=' * name_length)
print(full_name)
print('=' * name_length)
