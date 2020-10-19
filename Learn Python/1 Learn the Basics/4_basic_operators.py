number = 1 + 2 * 3 / 4.0
# print(number)

remainder = 11 % 3
# print(remainder)

# using two multiplication signs makes a power
squared = 7 ** 2
cubed = 2 ** 3
# print(squared)
# print(cubed)

# string concatenation
helloworld = "hello" + " " + "world"
# print(helloworld)

lotsofhellos = "hello" * 10
# print(lotsofhellos)

# joining lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
# print(all_numbers)

# repeating lists is the same as repeating strings
print([1, 2, 3] * 3)

# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively.
# You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.
x, y = "foo", "bar"
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
# print(x_list)
# print(y_list)
print(big_list)
