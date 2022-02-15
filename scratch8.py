#Strings in python
'''Note : Pyrhon doesn't support char data type 'c' it also considered as a string of length 1'''
str = "This is a String!"
str1 = 'This is a string'
str2 = '''This is also an string declaration''' # it is used for multiline string
print(type(str2))
print(str2)

# string index start from 0 we can acess string through a index
print('This is a first character of string :',str[0])

#acess every char in string using loop

name = 'CodexRitik'
for i in range(len(name)):
    print(name[i],sep=',',end = ' ')
print()

for i in name:
    print(i,sep=',',end = ' ')
print()

#slicing in python this is used to access the individual characters of the strings s[:] colon is also used in python to access the substring from the given string 

print(name[:])
print(name[0:]) # it is same as before

#Slicing : String[start:end-1] if we don't initialise it consider till last val
#Example : C o d e x R i t i k
#Example : 0 1 2 3 4 5 6 7 8 9
s = name[1:] #start 1st index to end
print(s)
s = name[0:5] # start 0th index to 4th index
print(s)
s = name[5:len(name)] # start from 5th index go till end
print(s)

'''We can do negative slicing also'''
# for accessing last char we may use -1 index similarly for 2nd last Char use -2

#Example : C o d e x R i t i k
#Index  :-9 -8 -7 -6 -5 -4 -3 -2 -1

#reverse print
print(name[::-1])

s = name[-1]
print(s) #last char
s = name[-1:-6] #it doesn't print anything 
print(s)
s = name[-6:-1]
print(s) # it print

#Reassigning Strings
str = "Hello"
str = str[1:4]
print(str)

#we can delete entire string using del keyword
str = 'CodexRitik'
del str
print(str)

'''Operators in String

1. + it is used to concatenate
2. * It is repetition operator
3. [] It is known as slice operator
4. [:] it is known as range of slicing
5. in it is known as memnbership operator it returns true if object is present
6. not in It is also work same but if not present then true
7. % it is used to perform string formatting

'''

name = "Ritik"
print(name*3) # it will print RitikRitikRitik
name2 = "Codex"
print(name2 + name)#concatenate two strings
print('R' in name)
print('C' not in name2)
print("Name : %s"%(name2+name))

 
'''Escape seuquence in String
1.\newline - it ignores the new line 
2. \\ Backslash - print '\'
3. \' single quotes - it prints '
4. \\" double quotes - it prints "
5. \a Ascii Bell
6. \b Ascii backspace - remove space in between
7. \f Ascii formfeed 
8. \n new line - print in newline
9. \r Ascii Carriege Return 
10. \t Horizontal tab
11. \v vertical Tab
12. \ooo character with octal value
13. \xHH character with hex value

'''

# format() method in string : The format() method is the most flexible and useful method in formatting strings. The curly braces {} are used as the placeholder in the string and replaced by the format() method argument. 

#Using curly braces
print("{} and {} both are the Best Friend".format("Rohan","Ritik"))

# Positional arguments
print("{1} and {0} are best".format("Ritik","Ritik"))

#keyword argument
print("{a},{b},{c}".format(a ="Mai",b="Ritik",c="hu"))

#String formatting using %operator

age = 20
height  = 5.7
name = 'Ritik'
print("Hii I am %s\nI am %d year old\nI am %f feet tall"%(name,age,height))

