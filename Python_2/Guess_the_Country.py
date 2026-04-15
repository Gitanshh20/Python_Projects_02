import random 

print("Guess the Country Game:-\n")

Country = ["India", "Australia","America","UK" or "United Kingdom","France","Russia","Canada"]

Choice = random.choice(Country)

Guess = 0

while True:

    User = input("Enter Your Guess: ")

    if User == Choice:
        print(f"Congrats🎉, You win the Country is {Choice} and You Take {Guess} Attempts.")
        break

    else:
        print("\nNot Correct, try agian\n")
        Guess += 1