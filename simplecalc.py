print ("Welcome to Nova Number Guessing's Simple 4-Operation Calculator")

startcalc = input("Press enter to begin calculating")

operationcalc = input("Enter your operation you will be Calculating with... (+ - * /): ")
numuno = float(input("Enter First Numeral"))
numdos = float(input("Enter Second Numeral"))

if operationcalc == "+":
    answer = numuno + numdos
    print(round(answer, 3))
elif operationcalc == "-":
    answer = numuno - numdos
    print(round(answer, 3))
elif operationcalc == "*":
    answer = numuno * numdos
    print(round(answer, 3))
elif operationcalc == "/":
    answer = numuno / numdos
    print(round(answer, 3))
else:
    print(f"{operationcalc} is not a valid mathmatical operation. Try again by rerunning the script.")
