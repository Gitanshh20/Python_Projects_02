import os
os.system('cls' if os.name == 'nt' else 'clear')

# A = P(1 + r/100)power n
#CI = A - P

print("Finder of CI".center(110))

class Compound_Interest :

    def __init__(self, Pirncipal, Rate, time):
        self.Pirncipal = Pirncipal
        self.Rate = Rate
        self.time = time
        
    @property
    def CI(self):
        print("CI is:",(((1 + (self.Rate / 100))** self.time)*self.Pirncipal) - self.Pirncipal)

Ask = Compound_Interest(int(input("Enter Your Principal:- ")),int(input("Enter Your Rate:- ")),int(input("Enter Your Time:- ")))

Ask.CI