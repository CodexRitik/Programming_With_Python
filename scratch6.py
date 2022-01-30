''' For Loops In Python'''

#for loop
#syntax of range = range(start,stop,step size) by default step is increment with 1 like java i++;
from os import sep


for num in range(5):
    print(num,end = ' ')#output 0 1 2 3 4
print()

str = "CodexRitik"

for char in str:
    print(char)

list = [1,2,3,4,5,6,7,8,9,10]
#syntax for varname in sequence: then statements
for i in list:
    print(i*2,end = ' ')
print()
sum = 0
for k in list:
    sum+=k
print('Total Sum :',sum)

print('Odd NumberS :')
for i in range(1,10,2):
    print(i,end = ' ')
print()

#Nested for loop

for k in range(5):
    for j in range(2):
        print(k,'*',j,'=',k*j)
print()

'''You may also use else condiiton with for loop'''
for i in range(4):
    for j in range(2):
        print(j+1,sep=',',end = ' ')
    print()
else:
    print('Loop Terminated')
