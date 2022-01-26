#Data Types in python
# 1.Numbers 2. sequence type 3. Boolean 4. set 5.Dictionary 
"""
Numbers - Integers,Complex Number ,Float
Sequence types - Strings,List,Tuple
"""
a = 5
#this is a integer
b = 40.5
#this is type of float
c = 1+3j
#this is a complex number

"""
Keywords in python : 
asset def class continue break
else finally elif del except
global for if from import
raise try or return pass
nonlocal in not is lambda
"""
# True - it represents Boolean true
# False - it represents Boolean false
# and - operator it's like &&
# or - operator it's like ||
# not - it is logical operator makes true to false and false to true
# assert - it is used to debugging tool in python, it checks the correctness of the code example :
a = 10
b = 0
print('a is dividing by Zero')
assert b!= 0
print(a/b)

#def - it is used to declare the function in python

def add():
    a = 10
    b = 20
    print(a+b)
add()

#class - It is used to represents the class in python
class Myclass:
    def func(self):
        pass

#continue - it is used to stop the execution of the current iteration

n = 0
while n < 4:
    n += 1
    if n == 2:
        continue
    print(n)

# break - it is used to terminate the loop execution 
for i in range(5):
    if(i == 3):
        break
    print(i)
print('End of execution')

#if it is used to represent the conditional statement 
i = 18
if(1 < 12):
    print("I am less than 18")

#else it is used with if statement when if statement returns false,then else block is executed.

num = 10
if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

#elif : it is used  when if condition is false then it will be executed

num = 20
if(num == 10):
    print('Ten')
elif(num == 20):
    print("Twenty")
else:
    print("Nothing")

#del - it is used to delete the ref of the object

a = 10
del(a)

#try,except - the try except is used to handle the exceptions.
a = 0
try:
    b = 1/a
except Exception as e:
    print(e)

#raise - the raise keyword is used to through the exception forcefully
a = 5
if(a > 2):
    raise Exception('a should not exceede 2')

# finally - the finally keyword is used to create a block of code that will always be executed no matter the else block raises an 

a = 0
b = 5
try:
    c = b/a
    print(c)
except Exception as e:
    print(e)
finally:
    print("Finally executed")

# for,while - both are used for iteration
list = [1,2,3,4]
for i in list:
    print(i)

a = 0
while(a < 5):
    print(a)
    a = a+1

#import - the import keyword is used to import modules in the current python script
import math
print(math.sqrt(25))

#from - it is used for import the specific function or attributes in the current python script

from math import sqrt
print(sqrt(25))

# as - it is used to create a name alias .It provides the user-define name while importing a module

import calendar as cal
print(cal.month_name[5])

# pass - the pass keyword is used for execute nothing or create a placefolder for future code, if we declare an empty class or function ,it will give an error so we use the pass keyboard to declare any empty class or function

class my_class:
    pass
def myfun():
    pass

#return - it is used to return the result value or none to called function

def sum(a,b):
    c = a+b
    return c
print("The sum is :",sum(10,15))

# is - it is used to check if the two var refers to the same object it will return true or false

x = 5
y = 5
a =[]
b = []
print(x is y)
print(a is b)

#global - it is used to create a global variable inside the function ,Any func can access th global var

def twoSum():
    global a
    a = 10
    b = 5
    print(a+b)
twoSum()
def fun():
    print(a)
fun()

#nonlocal - it is similar to the global and used to work with a var inside the nested function

def outside_func():
    a = 20
    def inside_func():
        nonlocal a
        a = 30
        print("Inner value :",a)
    inside_func()
    print('Outer Value :',a)
outside_func()

#lambda - the lambda keyword is used to create the anonymous function in python.it is an inline function without a name

a = lambda x : x**2
for i in range(1,4):
    print(a(i))

#yield - the yield keyword is used with the python generator.it stops the functions execution and returns value too the calller

def fun_gen():
    yield 1
    yield 2
    yield 3
for v in fun_gen():
    print(v)

#with - this is used in the exception handling .it makes code cleaner and more readable . the advantage of with ,we don't need to call close()

with open('file_path','w') as file:
    file.write('hello world!')

