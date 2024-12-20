print ("Welcome to Nova Number Guessing Version 1.1")

input("Press any key then press enter to begin playing")

import random

low = 1
high = 25
tries = 0
number = random.randint(low,high)

while True:
    guess = int(input(f"Guess the number... It will be between ({low} - {high}):"))
    tries += 1

    if guess < number:
        print (f"{guess} is too low")
    elif guess > number:
        print (f"{guess} is too high")
    else:
        print (f"{guess} is right!")

        print(f"This round took you {tries}")

    playagain = input (f"Do you want to guess again? If so, press enter")
    guess = random.randint(low,high)
