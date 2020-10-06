import random
class Zoo():
    def __init__(self,hunger,boredom):
        self.hunger = hunger
        self.boredom = boredom

    def mood(self):
        unhap = self.hunger + self.boredom 
        if unhap >= 15:
            m = "-1" 
        elif 15 > unhap >= 10:
            m = "0"  
        elif 10 > unhap >= 5:
            m = "1"  
        elif unhap < 5:
            m = "2"          
        return m, unhap, self.hunger, self.boredom

    def feed(self):
        a = int(input("A "))
        self.hunger -= a
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        b = int(input("B "))
        self.boredom -= b
        if self.boredom < 0:
            self.boredom = 0

def main():
    n = int(input("How many animals? "))
    o = 10000
    animals = dict()
    for i in range(n):
        h = random.randint(0,10)
        bor = random.randint(0,10)
        animals[i] = Zoo(h,bor)
    while o !=0:
        m = int(input("M(0=настроение,1=еда,2=игра) ")) 
        if m == 1:
            for i in range(n):
                animals[i].feed()
            continue
        elif m == 2:
            for i in range(n):
                animals[i].play()
            continue
        elif m == 0:
            for i in range(n):
                print(animals[i].mood()) 
            continue       

main()
