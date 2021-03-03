# customize the function with an input
# parameter is the name of the data/variable (name in this case)
# argument is the actual value of the parameter (jacob in this case)
#
# def greet(name):
#     print(f'hello {name}')
#     print('hello')
#     print('hello')
#
# greet('jacob')
#
# # be more explicit with keyword arguemnts
# def greet_with(name,location):
#     print(f'hello {name}')
#     print(f'What is it like in {location}?')
#
# greet_with(name='jacob',location='hawaii')
#
# import math
#
# def paint(height,width):
#     coverage = 5
#     cans = math.ceil((height * width) / coverage)
#     print(f"You need {cans} cans of paint")
#
# paint(2,4)

# prime number checker
def prime_check(number):
    prime = 'Y'
    for i in range(2,number-1):
        if number%i == 0:
            prime = 'N'
            break
    print(prime)



n = int(input("Check this number:"))
prime_check(n)




