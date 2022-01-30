'''Decision making Statements'''

#if statements

num = int(input('Enter The Number :'))
if(num %2 == 0):
    print('Even Number')

# if-else Statements

age = int(input('Enter Your Age :'))
if(age >= 18):
    print('You are Young Boy or girl!')
else:
    print('You are child!')


# if - elif -else statements

number = int(input('Enter a num :'))

if(number == 0):
    print('Number is Zero')
elif(number > 0):
    print('Positive Number')
else:
    print('Negative Number')


#You may also write nested conditional statement

num1 = 10
num2 = 20

if(num1 == 10):
    if(num2 >= 20):
        print("Number is greater or equal 20")
    else:
        print('Number is less then 20')
