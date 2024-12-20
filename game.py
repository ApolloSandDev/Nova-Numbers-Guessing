print ("Welcome to Numbers Guessing")

import random

low = 1
high = 25
guesses = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Enter number between ({low} - {high}):"))
    guesses += 1

    if guess < number:
        print (f"{guess} is too low")
    elif guess > number:
        print (f"{guess} is too high")
    else:
        print (f"{guess} is right!")
        break

    print (f"This round took you {guesses}")
