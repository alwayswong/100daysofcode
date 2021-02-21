import random
#  # easy coin flip generator
# x = random.randint(1,2)
# if (x == 1):
#     print("Heads")
# else:
#     print("Tails")
#

# assign a random person to pay for everyone's meal
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# rand = random.randint(0, (len(names) -1))
#
# print(f'{names[rand]} is going to buy the meal')

# index out of range error is just that youre asking for an item that is bigger than our list

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vert = int(position[1])
#
# # find the exact cooridnates to go and put the treasure in
# map[vert - 1][horizontal - 1] = 'X'
#
# print(f"{row1}\n{row2}\n{row3}")



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# TODO take input
while True:
    user = int(input("0 = Rock, 1 = Paper, 2 = Scissors?"))
    if user in (0,1,2):
        print(f"You chose: {user}")
        break
    else:
        print("Enter a valid choice")
# TODO generate random output as opponent
computer = random.randint(0,2)

# TODO describe game


if (user == 0):
    print(rock)
elif (user == 1):
    print(paper)
else:
    print(scissors)

print(f"Computer chose: {computer}")

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)
# TODO tell the user if they won or lost

if computer == user:
    print("Tie!")
elif computer == 0 and user == 1:
    print("You Win")
elif computer == 1 and user == 0:
    print("You Lose")
elif computer == 0 and user == 2:
    print("You Lose")
elif computer == 2 and user == 0:
    print("You Win")
elif computer == 2 and user == 1:
    print("You Lose")
elif computer == 2 and user == 1:
    print("You Win")
else:
    print("You are a super genius")

