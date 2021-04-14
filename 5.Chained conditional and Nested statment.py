'''
Nested statment mean here in one condition have many if but it should be indented
one after another .like below '''
'''
chaine condition mean here more than one condition include in one chake by
using (and , or ,not ) word
'''

#here chaine condition example
x = 2
y = 3

if not(x > y and x == y or x == 3):
    print('x is large number')
#nested if stadment

if x ==8:
    if x > y and x == 4:
        print(' ')
        print('x is large number')
        
    elif y > x and y == 3:
        print(' ')
        print(' y is large number')
else:
    print('bouth are equal ')
