# At the beginning we have a dictionary:
# my_new_dict = {'m': 12345, 'n': 32145, 'o': 54321, 'p': 23232, 'q': 43210, 'r': 13579}
#Your task is to complete the following instructions:
# -First of all we want to get the key which has alphabetically the maximal value - maximal_value_of_key,
# -second step is print that value out,
# -if maximal value in our dictionary is greater than the value of our maximal key (maximal_value_of_key), we want to delete the whole item under key maximal_value_of_key.
# - finally we want to print our new modified dictionary.

my_new_dict = {'m': 12345, 'n': 32145, 'o': 54321, 'p': 23232, 'q': 43210, 'r': 13579}
maximal_value_of_key = max(my_new_dict.keys())
print(maximal_value_of_key)

if max(my_new_dict.values()) > my_new_dict[maximal_value_of_key]:
    #my_new_dict.pop(max(my_new_dict.keys()))
    del my_new_dict[maximal_value_of_key]
print(my_new_dict)
