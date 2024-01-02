#used to store multiple items in a single variable
#list items are ordered, changeable, and allow duplicate values, starts at index 0
#list data types - int, int, bool

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
fruits = ["apple", "banana", "cherry"]
print(fruits)

#list items are ordered, changeable, and allow duplicate values
#items in a list - len() function
cars = ["audi", "bmw", "toyota", "nissan"]
print(len(cars))

#you can use the list constructor when creating new lists
mylist = list(("apple", "banana", "cherry"))

#accessing items in a list
mfruits = ["apple", "banana", "cherry"]
print(mfruits[0])

#you can specify range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#change items in a list
ff = ["apple", "banana", "cherry"]
ff[1] = "blackcurrant"
print(ff)

#insert items - use the insert method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add an item at the end of list - use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#add elements from another list to the current list - use extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove specified item - use remove() method
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#remove specified index - use the pop() method
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#del keyword removes specified index, or delete entire list
#clear - empties the list