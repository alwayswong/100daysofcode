############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import art
import random

# multiple tens are face cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)
print("Welcome to 21 - Let's Get Rich!\n")

dealer1 = random.choice(cards)
dealer2 = random.choice(cards)
dealer = [dealer1,dealer2]
showable_dealer = [dealer1,"X"]

player1 = random.choice(cards)
player2 = random.choice(cards)
player = [player1,player2]
player_sum = sum(player)

move_on = False

print(f"The dealers hand is showing {showable_dealer}")
print(f"Your hand is {player} for a total of {player_sum}")

# check initial blackjacks
if dealer1 + dealer2 == 21 and player1 + player2 == 21:
    print("You and the dealer both have Blackjack. Tie!")
    quit()

elif dealer1 + dealer2 == 21:
    print("Dealer has Blackjack - You lose :(")
    quit()

elif player_sum == 21:
    print("You have Blackjack - You win :)")
    print(art.win_sign)
    quit()

while move_on == False:
    hit = input("Hit or stand?").lower().strip()
    if hit == 'hit':
        new_card_player = random.choice(cards)
        player.append(new_card_player)
        print(player)
        print(f"Your score is {sum(player)}")
        if sum(player) > 21:
            # changing aces from 11 to 1 in the case of a bust
            for card in player:
                if card == 11:
                    card = 1
            if sum(player) > 21:
                print("Bust - you lose")
                quit()

    elif hit == 'stand':
        print(f"Your hand is {player} for a total of {sum(player)}")
        print(f"The dealer has {dealer} for a total of {sum(dealer)}\n")
        move_on = True


move_on_dealer = False
while move_on_dealer == False:
    while sum(dealer) < 17:
        print("Dealer hits")
        new_card_dealer = random.choice(cards)
        dealer.append(new_card_dealer)
        print(f"The dealer has {dealer} for a total of {sum(dealer)}")

    if sum(dealer) > 21:
        for card in dealer:
            if card == 11:
                card = 1
        if sum(dealer) > 21:
                print("Dealer busts - you win")
                print(art.win_sign)
                quit()

    if 16 > sum(dealer) > 22:
        print(f"The dealer stands with {dealer} for a total of {sum(dealer)}")





    if sum(player) == sum(dealer):
        print(f"The dealer and player have {sum(player)}. Tie!")
        quit()
    if sum(player) > sum(dealer):
        print("You win!")
        print(art.win_sign)
        quit()
    if sum(player) < sum(dealer):
        print("You lose!")
        quit()










##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

