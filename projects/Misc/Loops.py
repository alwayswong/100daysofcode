# fruits = ['Apple','Peach','Pear']
# practice 1
# for fruit in fruits:
#     print(fruit)
#     print(fruit + 'Pie')

# cum_height = 0
# counter = 0
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#   cum_height = cum_height + student_heights[n]
#   counter = counter + 1
#
# print (round(cum_height / counter,0))

# practice 2
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# high = 0
# for i in range(0,len(student_scores)):
#     if (student_scores[i] > high):
#         high = student_scores[i]
#     else:
#         continue
#
#
# print(f'The highest score is {high}')

# practice 3, evens
# total = 0
# for i in range(1,101):
#     if i%2 == 0:
#         total = total + i
#     i = i + 1
# print(total)

# FizzBuzz
# for i in range(1,101):
#     if i%15==0:
#         print('Fizzbuzz')
#     elif i%5==0:
#         print('Buzz')
#     elif i%3==0:
#         print('Fizz')
#     else:
#         print(i)
#
#     i = i + 1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# for letter in range(nr_letters):
#     print(random.choice(letters), sep='',end='')
#
#
# for symbol in range(nr_symbols):
#     print(random.choice(symbols), sep='',end='')
#
# for number in range(nr_numbers):
#     print(random.choice(numbers), sep='',end='')

#randomize the whole thing
password = []

for letter in range(nr_letters):
    password.append(random.choice(letters))

for symbol in range(nr_symbols):
    password.append(random.choice(symbols))

for number in range(nr_numbers):
    password.append(random.choice(numbers))

# now randomize
for i in password:
    print(random.choice(password), sep='',end='')