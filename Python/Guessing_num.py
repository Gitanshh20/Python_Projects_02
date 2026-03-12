
import os
os.system('cls' if os.name == 'nt' else 'clear')

print("--Guessing The Number--".center(110))

Opt = input("Are You Want to Play Game Y/N:- ")

def print_Statement1():
    if Opt == "Y":
        print("\nOk, Think a Number Between 1 - 9\n")

print_Statement1()    

if Opt == "Y":  
    Ask1 = input("Are You Thinked So print Y:- ")

def print_Statement2():
    if Opt == "Y":
        if Ask1 == "Y":
            print("\nThen Multiply Your Number with 2\n")
        
print_Statement2()

if Opt == "Y":  
    Ask2 = input("Are You Thinked So print Y:- ")

def print_Statement3():
    if Opt == "Y":
        if Ask2 == "Y":
            print("\nAfter Multiply Add it 10 in Your Number\n")

print_Statement3()

if Opt == "Y":  
    Ask3 = input("Are You done So print Y:- ")

def print_Statement4():
    if Opt == "Y":
        if Ask3 == "Y":
            print("\nAfter Multiply Divide Your Number by 2.\n")

print_Statement4()     

if Opt == "Y":        
    Ask4 = input("Are You d So print Y:- ")
        
def print_Statement5():
        if Opt == "Y":
            if Ask4 == "Y":
                print("\nThen After Divide Subtarct Your Number with Your Fisrt Number between 1 - 9 You Thinked\n")

print_Statement5()


if Opt == "Y":        
    Ask5 = input("Are You d So print Y:- ")

def Answer():
    if Opt == "Y":
        if Ask5 == "Y":
            print("\nYour Answer is 5")
        else:
            print("OK we play The GAme Next Time Bye!!")

Answer()
