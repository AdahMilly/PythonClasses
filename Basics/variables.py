'''
variables are reserved memory locations to store values
variables are created when you assign a value to it
'''

#example
name = "Mildred"
Name = "Mildred"

z = 2.1

'''
naming convention
must start with a letter or an underscore character
cannot start with a number
can only contain alpha-numeric characters and underscores
case sensitive
cannot be any of the py keywords
'''

#case sensitive
b = "Pilau"
B = "Byriani"

y=3
x="Mildred"

print(x)
print(y)

'''
variable casting-used to specify data type
example ; x = int(3)
'''

#type() - function used to get the variable type
x=1
print(type(x))

g = 3
print(type(g))
print(g)

#global variables- created outside the function, can be accessed from anywhere
x = "basics"

def anotherFuction():
  print("Learning basics")
  
anotherFuction()
def myfunction():
  print("Welcome to learning python " + x)

myfunction()