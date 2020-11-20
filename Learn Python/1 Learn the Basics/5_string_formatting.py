name = "John"
print("Hello, %s!" % name)

mylist = [1, 2, 3]
print("mylist: %s" % mylist)

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# exercise: You will need to write a format string which prints out the data using the following syntax:
# Hello John Doe. Your current balance is $53.44.

name = "John Doe"
balace = 53.44000
print("Hello %s, your balance is $%.2f" % (name, balace))
