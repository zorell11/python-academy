# Create a program, that will use the indexing to print and extract:
#first 5 letters in word 'indexing' and store it in variable first_five,
#last 5 letters in word 'indexing' and store it in variable last_five,
#every third letter, beginning with the first and store it in variable each_third
#Example of running program:
#First five letters: index
#Last fice letters: exing
#Every third letter: ien
#Save each slice in a variable and then print variable in sentence in the same way like in the example above('First five letters: ' + variable).


# Extract and print first 5 letters
first_five = 'indexing'[:5]

# Extract and print last 5 letters
last_five = 'indexing'[-5:]

# Extract and print each 3rd letter
each_third = 'indexing'[::3]

print("First five letters: " + first_five)
print("Last fice letters: " + last_five)
print("Every third letter: " + each_third)
