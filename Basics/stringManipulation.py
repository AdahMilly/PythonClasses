#represents characters, square brackets can be used to access elements in a str

x = "This will be fun"
print([3])

#multiline string
#use three double quotes or sinle triple quotes

b = """
learning python
for data
analysis
"""
#looping through a string
#use for loop to loop through a string
for x in "lemon":
    print(x)
    
#get the length
#use the len() function
a = "Ipsum fghhgtyujhfg"
print(len(a))

#in keyword - used to check if a certain phrase/character is present in a string
name = "Nyokoth"
if "h" in name:
    print("yeey got it")

#not keyword - check if character/phrase is not present in a string
txt = "Omena is sweet"
if "bad" not in txt:
    print("Omena is not bad, pthoooo")

#slicing - used to return a range of characters - you can slice to the end or from the start by leaving out the start/end range
g = "Hey, there"
print(g[2:5])

#negative indexing - used to start slicing from the end

#upper() - returns string to uppercase
a = "Hey"
print(a.upper())

#lower() - retyrns str to lowercase
b = "ddouble"
print(b.lower())

#strip() - remove any whitespaces
c = "bring coffee "
print(c.strip())

#replace - replace a string with another string
d = "Alot apoth"
print(d.replace("A", "H"))

#split() - splits a string into substrings
e = "master code online"
print(a.split())

#concatenate - combine two strings using +
f = "Hello"
g = "Will"
h = f + " " + g
print(h)

#read on escape characters
#string methods - https://www.w3schools.com/python/python_strings_methods.asp