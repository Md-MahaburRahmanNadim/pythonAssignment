'''
function decleration and called this function

sentext :
def nameOfFunction():   
    SOME block for the functionality of this function

 # here in the braket we can give many parameter seprating by cumma
 and when we called this function we have to put the argument

'''
def Sum(x,y):
    print(x + y)
    print(' ')
def Sub(x,y):
    print(x - y)
    print(' ')
Sum(4,5)
Sub(45,23)

# now combile this into one function

def sumSub(x, y):
    Sum = x + y
    Sub = x - y
    Mul = x * y
    print('Sum of those number = '+ str(Sum))
    print('Substraction of those number = ' + str(Sub))
    return Mul
print(sumSub(45,56))

'''
Warnning: one function have only one caractries becasue if you give many functinulity in a function than it might be confusiging 
and the function name must be apporete of the functionlity of this function 
becuase of user friendly ness 
'''
