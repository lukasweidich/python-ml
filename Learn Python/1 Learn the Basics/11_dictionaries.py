phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
# print(phonebook)

phonebook2 = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
# print(phonebook2)

# for name, number in phonebook.items():
# print("Phone number of %s is %d" % (name, number))

del phonebook2["John"]
phonebook2.pop("Jack")
# print(phonebook2.items())


# exercise:
# Add "Jake" to the phonebook with the phone number 938273443
# and remove Jill from the phonebook.
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}

# write your code here
phonebook["Jake"] = 938273443
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
