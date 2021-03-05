############DEBUGGING#####################

# # Describe Problem
# # bug is that the second number is not inclusive
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# # issue here is that indexing starts at 0. randint is inclusive so 0 to 5 is required
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0.5)
# print(dice_imgs[dice_num])

# # Play Computer
# # bug here is that you need 1994 to be included in one of the conditional statements
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

#Print is Your Friend
# # Bug is the double equals. use a print statement to realize you are not assinging the user input to the variable
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_words)

#Use a Debugger
# bug is the conditional flow
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])