#python literals - it can be defined as data that is given in a variable or constant

#String literals - it can be formed by enclosing a text in thye quotes.we can use both single as well as double to create a string

#single line string
text = "Hello"
#multi Line string
text1 = 'hello\
user'
text2 = '''welcome
to
Python world'''

#Numeric literals
# Int(signed Integers) Long(long integers) float(floating point ) Complex(complex)

x = 0b10100 #Binary Literals  
y = 100 #Decimal Literal   
z = 0o215 #Octal Literal  
u = 0x12d #Hexadecimal Literal  
  
#Float Literal  
float_1 = 100.5   
float_2 = 1.5e2  
  
#Complex Literal   
a = 5+3.14j  
  
print(x, y, z, u)  
print(float_1, float_2)  
print(a, a.imag, a.real)  

#Boolean Literals - it can have any of the two values : True or False 
x = (1 == True)  
y = (2 == False)  
z = (3 == True)  
a = True + 10  
b = False + 10  
  
print("x is", x)  
print("y is", y)  
print("z is", z)  
print("a:", a)  
print("b:", b)  

#List Literals :
list = ['Ritik',21,'CodexRitik'];
list1 = ['GLA',281406]
print(list+list1)

#Dictionary Literals
dict = {'Name':'CodexRitik','Age':18,'Univ Roll No:':191500658}
print(dict)

#Tuple is immutable 
tup = (10,20,"Ritik",[1,2,3])
print(tup)

#Set
set = {'Apple','Grapes','Guava','Papaya'}
print(set)

