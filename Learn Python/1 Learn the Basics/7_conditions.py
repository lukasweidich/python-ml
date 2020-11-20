#x = 2
# print(x == 2)  # prints out True
# print(x == 3)  # prints out False
# print(x < 3)  # prints out True

#name = "k"
#age = 23
#if name == "John" and age == 23:print("Your name is John, and you are also 23 years old.")
# else:print("your name is not john")
#if name == "John" or name == "Rick":print("Your name is either John or Rick.")

name = "Lukas"
if name in ["Lukas", "Weidich"]:
    print("accepted")

statement = True
if statement:
    print("true")

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False

# exercise
# change this code
number = 16
second_number = 0
first_array = [1,3,56]
second_array = [1, 3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
