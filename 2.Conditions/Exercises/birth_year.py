#Your task is to create a script called birth_year.py that will:
# -ask the user for his/her age
# -calculate the year the person was born in
# -print the resulting year

#Example of running the script:
#/Users/PythonBeginner/Lesson1$ python birth_year.py
#How old are you? 35
#You were (probably) born in 1982

age = int(input('How old are you? '))
current_year = 2020
born = current_year - age
print('You were (probably) born in', born)
