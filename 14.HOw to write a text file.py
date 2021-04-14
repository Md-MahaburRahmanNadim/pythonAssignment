'''
same thing like as read a file but in the read file video we forget
to close the file so we have to close the file otherwise it's run in background

'''
Open = open('write.txt' , 'w')

Open.write('Assalamolikum \n')
Open.write('\n My name is Md.Mahabur Rahman Nadim ')



Open.close()
