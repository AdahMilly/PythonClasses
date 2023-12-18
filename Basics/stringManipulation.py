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