#commnets in python single line
"""
This is multiline comments in python, it is also a string literals which is not assigned any variables it is ignored by pvm and assume that just like a comments
"""
print("Hello")
#type() func is used to identify a class of data items
print(type("hello"))

#suppose we assign a two varibale with same value 
a = 50
b = a
#then we know that in python every created object identifies uniquley in python
# it provides to check the id of objects id() function so we can check like
print(id(a))
print(id(b))
#it will give us same id because both refers same value
a = 500
print(id(a))
# now it will give us diffrent id
"""
valid variable name in python : Variable names can be any length can have uppercase, lowercase (A to Z, a to z), the digit (0-9), and underscore character(_), some examples are given below.
"""
name = "A"  
Name = "B"  
naMe = "C"  
NAME = "D"  
n_a_m_e = "E"  
_name = "F"  
name_ = "G"  
_namee = "H"  
na56me = "I"  
print(name,Name,naMe,NAME,n_a_m_e, NAME, n_a_m_e, _name, name_,_namee, na56me)  

#Camel Case : Example : nameOfStudent, valueOfVar
#pascal case : Example : NameOfStudent,StudentName
#Snake case : name_of_student,value_of_number

#Python suports multiple value assignment
x = y = z = 100
print(x,y,z)
a,b,c = 10,20,30
print(a,b,c)

#Variable types in python
# 1. Global variable 2 . Local variable

#Local variable is that which scopes only within the function
#Global var is used in hole program its scope in the entire program we can use inside or outside the function.

#Defining a function
def add():
    #thease are local variables
    a = 20
    b = 30
    c = a+b
    print("The Sum is",c)
#calling the function
add()

#Defining a Global var in func

x = 101;
def mainFunction():
    #def var
    global x
    print(x)
    #modifying value
    x = "Welcome To Programming"
    print(x)
mainFunction()
print(x)

#we can delete a var using del keyword then var is no longer be in use
num = 10
print(num)
del num

#Maximum possible value of an integer it treats all integer values as an int data types

a = 10000000000000000000000000000000000000000000
a += 1
print(a,type(a))

#Tokens can be defined as a punctuator mark,reserved words and each word in a statement , the token is the smallest unit inside the given program

# keywords Identifiers Literals Operators
