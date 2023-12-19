'''
used to perform operations on variables and values
examples
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''

#arithmetic operators - used to assign values to variables
x=5 #assign

x += 3 #same a x=x+3
x -= 3 #same as x=x-3
x *= 3 #same as x=x*3
x /=3 #same as x=x/3
x %=3 #same as x=x%3
x //= 3 #same as x//3
x **= 3 #same as x**3
x &= 3 #same as x&3
x |= 3 #same as x|3 - set union operator
x ^= 3 #same as x=x^3
x >>=3 #same as x=x>>3
x <<=3 #same as x = <<3

#comparison operators - used to compare values
#equal == 
#not equal != 
#greater than >
#less than >
#greater than or equal to >=
#less than or equal to <=

#logical operators - used to combine conditional statements
#x < 5 and x < 10
#x < 5 or x < 4
#not(x # 5 and x < 10)

#identity operators - used to compare objects/not if they are equal but if they are the same object
#is
#is not

#membership operators - used to test if a sequence is presented in an object
#in x in y
#not in x not in y
x = ["apple", "banana"]

print("banana" in x)

#bitwise operators - used to compare binary numbers
'''
& and
| or
^ xor
not
'''