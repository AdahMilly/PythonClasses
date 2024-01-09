#python has the following data types
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

we use the type function to get the python data type
'''
#python numbers
y=4 #int - whole number, positive/negative without decimals, of unlimited length
x=2.5 #float - positive/negative number containing one/more decimals
z=2j # complex - written with j as the imaginary part

#random numbers
#py has a random number module used to display random numbers

import random
print(random.randrange(1,100))

#strings
name = "Mildred"

#list - sequence data type used to store the collection of data, it is mutable
x= ["apple", "banana", "cherry"]
print(x[0])

#tuple - collection of objects separated by commas, it is immutable
x=("apple", "banana", "cherry")

#dict - used to store data in key value pairs
x = {"name" : "John", "age" : 36, "gender": "M"}

#set - a collection which is unordered, unchangeable*, and unindexed.
x = {"apple", "banana", "cherry"}

#bool - used to know if an expression is either true or false
x=False