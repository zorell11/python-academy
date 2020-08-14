#sentence = 'I do not want to work today'
rep = int(input("Enter the # of repetitions: "))
sentence = input("Enter the string: ")

lst = sentence.split()
result = []

while lst:
    word = [lst.pop(0)]
    word = word * rep
    result += word
result = ' '.join(result)
print(result)
