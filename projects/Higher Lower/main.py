import data
import art
import random


print(art.logo)
score = 0
while True:
    # generate comparison
    personA = random.choice(data.people)
    personB = random.choice(data.people)
    if personA["follower_count"] > personB["follower_count"]:
        winner = 'a'
    elif personA["follower_count"] < personB["follower_count"]:
        winner = 'b'
    else:
        print('tie')


    # Load a comparison
    print(f'Compare A: {personA["name"]}, a {personA["description"]}, from {personA["country"]}')
    print(art.vs)
    print(f'Compare B: {personB["name"]}, a {personB["description"]}, from {personB["country"]}')

    guess = input("Who has more followers? Type 'A' or 'B':\n").strip().lower()
    # Check right or wrong
    if guess == winner:
        score += 1
        print(f'Correct! Current score: {score}')
        print(f'{personA["name"]} has {personA["follower_count"]*1000000} followers')
        print(f'{personB["name"]} has {personB["follower_count"]*1000000} followers\n')
        continue
    else:
        print(f'Wrong! Final score: {score}')
        print(f'{personA["name"]} has {personA["follower_count"]*1000000} followers')
        print(f'{personB["name"]} has {personB["follower_count"]*1000000} followers')
        break
