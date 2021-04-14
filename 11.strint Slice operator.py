'''
Slice operator syntext
mantion any veriable where text exit and than [star:stop:step] like as
for loop range value

example :
text is a veriable so we can wright
text[start:stop:step]
'''
friends = ['Nadim','Hasan','Mahamudul',323,343,]
text = ' My name is Md.Mahabur Rahman Nadim'

print(friends[2])

# as well as we can use this tacqunic with string like below

print(' ')

print(text[5])

'''
but we can do this thing very quickly by using slice oprator

'''
print(text[2:6:2])
print(' ')
print(friends[0:3:3])

# to insert spacific lookition in list we use slice oprator
friends[0:0] = 'Robiul'
friends.append('robiul') # this is a approat way to insert something 
print(friends)
