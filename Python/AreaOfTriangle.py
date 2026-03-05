import os
os.system('cls' if os.name == 'nt' else 'clear')

# Calc of Area of Triangle
#formula = 1/2 * b * h

print("--Find Area of Triangle Using this-- \n".center(110))
class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def Area_finder(self):
        print("Your Area of Triangle =",float(1/2 * self.base * self.height))


Area = Triangle(float(input("1. Enter Your Base:- ")),float(input("2. Enter Your Height:- ")))
Area.Area_finder

