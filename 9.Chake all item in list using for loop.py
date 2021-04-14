friends = ['Mahamudul','Nadim','Shakib','Robiul']
for friend in friends:
    if friend == 'Mahamudul':
        print('Best friend ever')
        print(friend)
        print(' ')
    else:
        print('Good friend all of them')
        print(friend)
        print(' ')

''' anther way to do this '''
for x in range(0,4):
    if friends[x] == 'Robiul':
        print('going to be a  best friend ')
        print(' ')
    else:
        print(' Good friends all of them ')
        print(' ')
