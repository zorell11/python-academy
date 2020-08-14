#Try to access the value stored under the 'Level' key, which is stored under the 'Job' key
#inside the my_db dictionary.
#Try to concatenate the whole address into one string. City and Country should be separated
#by comma.

# Database
my_db = {   'Name': 'John Smith',
            'Age': 34,
            'Address': {'Street': 'Main',
                'Street #': 241,
                'City': 'Boston',
                'Country': 'Venezuela'},

            'Job': {'Job Title': 'System Admin',
                    'Level' : 3}
}

# 1
level = my_db['Job']['Level']

# 2
adress = my_db['Address']['Street'] + ' ' + str(my_db['Address']['Street #']) + ' ' + my_db['Address']['City'] + ', ' + my_db['Address']['Country']
# Print
print(level)
print(adress)
