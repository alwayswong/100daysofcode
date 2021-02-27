############### Blackjack Project #####################

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
import time

# multiple tens are face cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)
print("Welcome to 21 - Let's Get Rich!\n")
while True:
    while True:
        dealer1 = random.choice(cards)
        dealer2 = random.choice(cards)
        dealer = [dealer1,dealer2]
        showable_dealer = [dealer1,"X"]

        player1 = random.choice(cards)
        player2 = random.choice(cards)
        player = [player1,player2]
        player_sum = sum(player)

        move_on = False

        print(f"Your hand is {player} for a total of {player_sum}")
        print(f"The dealers hand is showing {showable_dealer}\n")


        # how do you not exit a loop but go back to the top?
        # check initial blackjacks
        if dealer1 + dealer2 == 21 and player1 + player2 == 21:
            print("You and the dealer both have Blackjack. Tie!")
            break

        elif dealer1 + dealer2 == 21:
            print("Dealer has Blackjack - You lose :(")
            break

        elif player_sum == 21:
            print("You have Blackjack - You win :)")
            print(art.win_sign)
            break

        while move_on == False:
            hit = input("Hit or stand?\n").lower().strip()
            if hit == 'hit':
                new_card_player = random.choice(cards)
                player.append(new_card_player)
                #print(player)
                #print(f"Your score is {sum(player)}")
                if sum(player) > 21:
                    # changing aces from 11 to 1 in the case of a bust
                    for card in player:
                        if card == 11:
                            player.remove(card)
                            player.append(1)

                            #print(player)
                    print(player)
                    print(f"Your score is {sum(player)}")
                    if sum(player) > 21:
                        print("Bust - you lose")
                        quit()
                else:
                    print(player)
                    print(f"Your score is {sum(player)}")

            elif hit == 'stand':
                print(f"Your hand is {player} for a total of {sum(player)}")
                print(f"The dealer has {dealer} for a total of {sum(dealer)}\n")
                move_on = True

        time.sleep(3)
        move_on_dealer = False
        while move_on_dealer == False:
            while sum(dealer) < 17:
                print("Dealer hits")
                new_card_dealer = random.choice(cards)
                dealer.append(new_card_dealer)
                if sum(dealer) > 21:
                    for card in dealer:
                        if card == 11:
                            dealer.remove(card)
                            dealer.append(1)
                    #print(dealer)
                    #print(f"Dealer score is {sum(dealer)}")
                    print(f"The dealer has {dealer} for a total of {sum(dealer)}\n")
                    time.sleep(3)
                    if sum(dealer) > 21:
                        print("Dealer busts - you win")
                        # print(art.win_sign)
                        break
                else:
                    #print(dealer)
                    #print(f"Dealer score is {sum(dealer)}")
                    print(f"The dealer has {dealer} for a total of {sum(dealer)}\n")
                    time.sleep(3)

            if 16 > sum(dealer) > 22:
                print(f"The dealer stands with {dealer} for a total of {sum(dealer)}")
                time.sleep(3)


            if sum(player) == sum(dealer):
                print(f"The dealer and player have {sum(player)}. Tie!")
                break
            if sum(player) > sum(dealer):
                print("You win!")
                #print(art.win_sign)
                break
            if sum(player) < sum(dealer):
                print("You lose!")
                break


        while True:
            new = input("\nPlay another game? (yes/no)").lower().strip()
            if new == 'yes':
                break
            elif new == 'no':
                quit()
            else:
                print("yes or no?")