'''
if we want to read something than we have to open this thing . than we can read
it . like this consept first open the file and than read the text file .
very simple

'''
openFile = open('Read.txt', 'r')

readFile = openFile.readlines()

print(readFile)
print(' ')

#working for removing \n or scape sequence it's come for prasing ENTER key in
# the keybord
errorFree = []
for scape in readFile:
    errorFree.append(scape[:-1])


print(errorFree)
print(' ')

# but here missing last line last letter in the list for fixing this

for scape in readFile:
    if scape[-1] == '\n':
        errorFree.append(scape[:-1])
    else:
        errorFree.append(scape)
print(errorFree)
print(' ')
'''
in this avobe codding we get some problem try to figer it why it's occur
because here we don't use empty list so that here we get some unexpect
list item from the aveboe list mistake list'''

# minemum fixing problem or max productivety
nerrorFree = []
for scape in readFile:
    nerrorFree.append(scape.strip())
print(nerrorFree)

    
openFile.close()
