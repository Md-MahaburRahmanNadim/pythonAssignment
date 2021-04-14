# .find() and .count()
'''

here work of find() function is to find the charecter first postion in the
string

and The work of count() function is to show the sum of how may charchter have
there like this one

'''

string = 'My name is Nadim . sdfdsfsdfljkjdsjhfiewrjowe'
print(string.find('f'))
print(' ')
'''
here if i have one letter in many times than find() function only show the
first letter postion number not letter or all of this repeted letter '''

print(string.find('y'))
print(string.find('l'))

'''
but here we can count how many times it's use here not postion'''

print(string.count('f'))
print(string.count('e'))
print(string.count('j'))

#some prectical uses

test = input('Enter strong password')
if test.count('_')> 0 and test.count('A') > 0 :
    print('Strong password')
else:
    print('Weak password')
