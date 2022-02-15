#Python List
'''
A list in python is used to store the sequence of various types of data.It is mutable type that means we can modify its element  after creation

'''

list = [] #blank list
list = ["Ritik",20,5.6]
list1 = [1,2,3,4,5]
print(type(list1))

#Lists maintain the order of the elements
#example :
list = ["Ritik",20,5.6]
list2 = [20,"Ritik",5.6]
print(list == list2)#print false
list3 = ["Ritik",20,5.6]
print(list == list3)#print true because it check the order of elements in list
l = [20,30,"Ritik",40,9,'char','A']

#printing elements using index

for i in range(len(l)):
    print(l[i],end=" ")
print()

l[2] = "Codex" # change the data on the specifies position
print(l)

#Slicing in list same as the string
#list[start:stop:step]   

list = [0,1,2,3,4,5,6,7,8]
print(list[0:])
print(list[1:5])
print(list[:5])

print(list[-1])#last element of list
list[-1] = 25#updating value in list
print(list)
n = 'Code'
l1 = []
l1 = list.extend(n)
print(l1)

fruits = ["Apple","Banana","Orange"]
for fruit in fruits:
    if(fruit == "Orange"):
        print("Yes Orange is already in List")

#some useful methods of list

animalList = []

#append()mehtod is used to add the item at the end of the list
animalList.append("Lion")
animalList.append("Rat")
print(animalList)

#insert() is used to insert the item at the specified index
animalList.insert(1,"Cow");
print(animalList)

#extend() method is used to append the another element in list
newList = ["Ziraffue","Tiger","Ox","Horse"]
animalList.extend(newList)
print(animalList)

#remove list items
animalList.remove("Tiger")
print(animalList)

#remove by index
animalList.pop(0)
print(animalList)

#remove last index
animalList.pop()
print(animalList)

#using del del animalList[0] or entire list del animalList
#or entire list can be delete using clear()

#Loop in the list
Lists = ["Yes","No","Yes","No"]
for ans in Lists:
    print(ans)
print()

#by index
for i in range(len(Lists)):
    print(Lists[i],end=" ")
print()

k = 0
while k < len(Lists):
    print(Lists[k],end=" ")
    k = k+1
print(Lists[::-1])#reverse lists using slicing

#Lists Comprehesion example
[print(x) for x in Lists]
