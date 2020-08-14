# Write a Python program that will create "echo sentences". Each word in the sentence we will feed in,
#should be repeated n number of times. The number of repetitions and the sentence to be manipulated
#are inputs provided by the user.
#Example:
#If the supplied number of repetitions is 3 and the sentence: 'I do not want to work today'.
#Output:
#'I I I do do do not not not want want want to to to work work work today today today'
#The resulting sentence cannot begin with space, unless the input sentence contained it.
#Example of running the script:
#$ python3 echo.py
#Enter the # of repetitions: 3
#Enter the string: I do not want to work today
#I I I do do do not not not want want want to to to work work work today today today


##############
repetition = int(input('Enter the # of repetitions: '))
sentence = input('Enter the string: ')
words = sentence.split()
result =[]

while words:
    word = [words.pop(0)]
    word *= repetition
    result += word
res = ' '.join(result)
print(res)
