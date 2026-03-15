import os
os.system ('cls' if os.name == 'nt' else 'clear')

import random

num = random.randint(1, 100)

print("Welcome to Number Guessing Python Program\n")

Ask = input("If You Want to Start Type 'Yes' or 'No' to denied:- ")

if Ask == "No":
  print("Ok, Bye We can Play Next Time")
  

if Ask == "Yes":
    def Guess_Loop():
        
        while True:
            
            if Ask == "Yes":
                Guess_num = int(input("Enter Your Guess: "))
                
            if Guess_num > num :
                print("\nToo High!, Try Again.")
                
            elif num > Guess_num :
                print("\nToo Low!, Try Again.")
                
            else:
                print("\nCongress, You are right this is your Number..")
                break


    Guess_Loop()
