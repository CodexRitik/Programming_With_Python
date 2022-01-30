#Operators in Python

'''ArithMetic Operators'''
num_1 = 20
num_2 = 10

print('Addition :',num_1 + num_2)
print('Subtraction :',num_1 - num_2)
print('Float Division :',num_1 / num_2)
print('Multiplication :',num_1 * num_2)
print('Remainder :',num_1 % num_2)
print('Exponent :',num_1 ** 2)
print('floor Division :',num_1 // num_2)

'''Comparison Operator'''

print('Equal :',num_1 == num_2)
print('Not Equal :',num_1 != num_2)
print('Less Then Or Equal :',num_1 <= num_2)
print('Greater Then Or Equal :',num_1 >= num_2)
print('Greater Then :',num_1 > num_2)
print('Less Then :',num_1 < num_2)

'''Assignment Operator'''
# = += -= *= %= **= //= thease all works similar the above discussed symbol this is a sort form to assign a value

#Example :
num1 = 10
num1 = num1 + 5
#it's same  like 

num1 += 5


'''Bitwise Operators'''
a = 7
b = 6
print("Bianry AND & :",a & b)
print('Binary Or | :',a | b)
print('Bianry xor ^ :',a ^ b)
print('Negation ~ : ', ~ a)
print('Left Shift :',a << 2)
print('Right shift :',b >> 2)

'''Logical Operators'''
# and if both are true
# or if one or both true
# not it is just opposite if true then false or vice varsa
num = 10
num2 = 20
if(num == 10 and num2 == 20):
    print('True')
if(num == 10 or num2 == 5):
    print('False')
b = False
print(not b)

'''Membership Operator'''

# in - It is evaluated to be true if the first operand is found in the second operand
# not in - It is evaluated to be true if the first operand is not found in the second operand 

num_List = [1,2,3,4]
if(2 in num_List):
    print('Found!')
if(3 not in num_List):
    print("True")
'''Identity Operators'''
# is - it will be true if the reference present in both sides point to the same object
# is not - it will be true if the reference present at both sides don't point to the same object

