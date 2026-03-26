import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Currency-Coverter..\n")

INR = 93.80
EUR = 0.86
JPY = 159.27
GBP = 0.75

 
print("1.Indian Rupee(INR)\n2.Euro(EUR)\n3.Japanese Yen(JPY)\n3.British Pound(GBP)\n")

amount = float(input("Enter Your Amount in USD: "))

choose_Currency = int(input("Choose Your Converter: ")) 

def Converter():
    if choose_Currency == 1:
        print(f"{amount} USD = {amount*INR} Rupee")

    elif choose_Currency == 2:
        print(f"{amount} USD = {amount*EUR} Euro")

    elif choose_Currency == 3:
        print(f"{amount} USD = {amount*INR} Rupee")

    elif choose_Currency == 4:
        print(f"{amount} USD = {amount*INR} Rupee")

Converter()