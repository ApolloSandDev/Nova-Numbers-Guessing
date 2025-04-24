print ("          Welcome to the")
print ("-------| PRIME OR COMPOSITE |-------")
print ("          Number Checker")
print ("This program will check your entered number and tell you if it is prime or composite")
input ("Press enter to begin")

num = int(input("Enter a number:"))
if num < 1:
    print(" Number needs to be greater than one. Try again!")
elif num == 1:
    print(num,"is not prime or composite.")
else:
    for divisor in range(2, (num//2)+1):
        if (num % divisor) == 0:
            print(num," is a composite number")
            break
    else:
        print(num, "is a prime number")

print ("Thank you for using this program! Have a nice day! :)")






