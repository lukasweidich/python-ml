myint = 7
# print(myint)
myfloat = 7.0
# print(myfloat)
myfloatfromint = float(myint)
# print(myfloatfromint)
mystring = 'hello'
# print(mystring)
mystring = "hello"  # strings can use double or single quotes
# print(mystring)
mystring = "I'm using single quotes within a string and it's not causing any problems!"
# print(mystring)

one = 1
two = 2
three = one + two
# print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
# print(helloworld)

a, b = 3, 4
# print(a, b)

# mixing operators between string and numbers is not supported:
print(one + two)  # works fine
# print(one + world)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# exercise
# The target of this exercise is to create a string, an integer, and a floating point number.
# The string should be named mystring and should contain the word "hello".
# The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.

mystring = "hello"
myfloat = 10.0
myint = 20
