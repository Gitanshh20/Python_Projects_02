import os
os.system('cls' if os.name == 'nt' else 'clear')

# Triangle Shape of Stars
Num = int(input("Enter Your Num: "))

for i in range(1, Num+1):
    print(" " * (Num - i), end="")
    print("*" * (2 * i- 1))

#Normal Pattern Of Stars
Num = int(input("Enter Your Num: "))

for i in range(1, Num+1):
    print("*"*i)

