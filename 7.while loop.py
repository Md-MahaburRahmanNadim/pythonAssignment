'''
sentext of while loop

while condition true:
    do this

in this loop here no pre define breaking point if this loop is gonna true .
we have to put the break keyword to break this loop otherwise it's run life time

example below
'''
loop = True

while loop:
    name = input('Any password but stoung one: ')
    if name == 'NadiM':
        #loop = False
        break

