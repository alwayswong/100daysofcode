import random
import wordlist
import art


word_list = wordlist.word_list

#Randomly choose a word from the word_list and assign it to a variable.
word = random.choice(word_list)

#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []

lives = 6



for i in range(len(word)):
    display.append("_")
    #print(display)

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
print("Welcome to Hangman")
print(art.logo)
print(f'word is {word}')
while True:
    guess = input("Guess a letter: ").lower()

# check the letter that the user inputs
# you can also use for, range loop to access the indices
    for inx,letter in enumerate(word):
        if guess == letter:
            display[inx] = guess
            #print("Correct")
    if guess not in display:
        lives = lives - 1
        print(f"Lives left: {lives}")
        print(art.stages[lives])
        if lives == 0:
            print("Loser!")
            quit()
# this prints the display word without all the annoying parts of a list
    print(f"{' '.join(display)}")
    if "_" not in display:
        print("You win")
        quit()

