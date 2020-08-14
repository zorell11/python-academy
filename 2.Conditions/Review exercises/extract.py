#### find method

email1 = 'mr.reilly@gmail.com'
email2 = 'john55@yahoo.com'
email3 = 'elgringo@atlas.sk'

index1 = email1.find('@')
index2 = email2.find('@')
index3 = email3.find('@')

print(email1[:index1])
print(email2[:index2])
print(email3[:index3])



#### split methods

email1 = 'mr.reilly@gmail.com'
email2 = 'john55@yahoo.com'
email3 = 'elgringo@atlas.sk'

print(email1.split('@')[0])
print(email2.split('@')[0])
print(email3.split('@')[0])
