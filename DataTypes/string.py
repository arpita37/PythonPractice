print('hello')
print('hello')
print("This is also a string")
print('Hello world')
print("I'm going on a run")
#escape sequence
print("Hello \t Space")
print("HEllo\nspace")
print(len("Hello!   "))


### Indexing
mysting = "Hello Word"
print(mysting[1])
print(mysting[-2])
print(mysting[1:100]) ### ending will be min(end_idx, len(string)-1)
print(mysting[2:])
print(mysting[::2])


### Properties and methods


# 1. Immutability
name = "Sam"
#name[0] = "p" #TypeError: 'str' object does not support item assignment
print("P"+name[1:])

# 2. Methods 
x = "   abc"
print(x.upper()) ## not in place
print(x.lower())
print(x.capitalize())
print(x.casefold())
print(x.strip())

# Print formatting with String
## .format()
print("I am {}. My age is {}".format('Arpita Basak', 26))
print("The {} {} {}".format('fox','brown','quick'))
print("The {2} {1} {0}".format('fox','brown','quick'))
print("The {q} {b} {f}".format(f = 'fox',b = 'brown',q = 'quick'))



### Precision with floats " {value:width.precision f"}" width -> how many whitespace in front of number
result  =1100/777
print(result)
print("the value is {r:4.5f}".format(r = result))

## fstrings
f = 'first'
print(f"This is my {f} fstring")