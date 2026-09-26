def print_numbers(*numbers):

    for num in numbers:
        print(num)

    print(numbers)

print_numbers(1,2,3,7)
print_numbers(1,7)


#using greet function


def greet(roll,name):
    print(name,roll)

greet(name="rohan",roll=147)
greet(123,"rohan")


#by making dictionary
def greet(**data):
    print(data)

greet(name="sumit",roll=123,mobile=125665456)