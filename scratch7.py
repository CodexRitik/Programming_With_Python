#while loop in python
'''Expression
while expression :
    Statements '''

i = 0
str1 = 'Codexritik'
while(i<len(str1)):
    if(str1[i]=='x'):
        print(' ')
    else:
        print(str1[i],end=' ')
    i = i+1

num = 10
while(num > 0):
    if(num==5):
        break
    print(num,end= ' ')
    num-=2

#print table using while
i = 1
number = 2
while (i <= 10):
    print("%d x %d = %d\n"%(number,i,number*i))
    i+=1

#else with while loop
i = 1
while(i <= 5):
    print(i)
    i += 1
else:
    print('Loop Over')


'''Fibonaci series'''

# seires example 0 1 1 2 3 5 8 13
terms = int(input('Enter the number of terms'))
a = 0
b = 1
if(terms <= 0):
    print('Enter the valid term value:')
elif(terms == 1):
    print('Fibonacci Series :',b)
else:
    print('Fibonacci Series :')
    while(terms > 0):
        print(a,end=' ')
        c = a+b
        a = b
        b = c
        terms -= 1

#Search in List item
list = [2,7,9,0,4,-1]
item = int(input('Enter the num'))
count = 1
for i in list:
    if(i == item):
        print('Item Found!')
        count += 1
        break; # it is used to terminate the loop
else:
    print('Not Found!')

#Use of continue in python
#It is used to skip the value in loop it terminate the iteration of program and start next iteration
print('Continue Statements :')
num = 10
while(num >= 0):
    num -= 1
    if(num %2 == 0):
        print(num,end=' ')
    else:
        continue
print()

#pass it is used to execute noting mainly it is used for unused lines of code
for i in range(10):
    if(i <= 5):
        pass
    else:
        print(i,end=' ')
print()
