def my_greeting():
    print("Hallo!")
# my_greeting()


def my_greeting_with_arguments(greeting, name):
    print("%s %s!" % (greeting, name))
# my_greeting_with_arguments("Hallo", "Lukas")


def add(a, b):
    return a + b
# print(add(1, 2))

# exercise
# Modify this function to return a list of strings as defined above


def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"


def build_sentence(benefit):
    return "%s  is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


name_the_benefits_of_functions()
