print('My name is ')
Name = input()  # here defult data type is (string or str) so if we dill with this
#function with in integer than we have to change datatype for this veriable 
print(Name)
print(type(Name)) # here you can see this variable type is string or str

#here we do some mistake for this user input function defult value

print('Enter first number')
# num1 = input() # here we have to change defolt data type to int only for
#math opration. because in math we dill with int data type if we put str data type instade of int than we get an error now if we run this line than we get an error when we sum num1 and num12 variable that 
''' why in next line we chage str data type to int data type by type custing '''
num1 = int(input())

print('Enter the secound number')
num2 = int(input())

SUM = num1 + num2
print(SUM)

print('here we get string concatination result . but we want sum result wright')
#how can we do that. just change the data type of the variable into int

Rsum = int(num1) + int(num2)
print('wright sum ' + str(Rsum))


# now there time to know about some oprator

# +,-,*,/ those oprator use in math so we know about those

print('Application of simple math opration ')
AofOprator = num1 / num2
print(' ')
print(AofOprator)

# new one is

# ** this call power some thing or expontial
print(' ')
print('applicaion of square or exponialtial oprator (**)')
print(num1 ** num2)
# // this use for integer devition not for float devition . this result show
print('applicaion of integer or hole number divition oprator (//) ')
print(num1 // num2)
print(' ')
# the hole number only 
# % it's give us rimender or bug shes

print('Example of rimender (%)')

print( num1 % num2)





