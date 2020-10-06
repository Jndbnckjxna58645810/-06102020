from tkinter import *
import random
import time
import math
class Critter2_:
    """Critter2_0"""
    total = 0

    @staticmethod
    def status():
        print('Общее число зверюшек', Critter2_.total)

    def __init__(self,name,color,x,y,canvas,a,d,hunger,boredom,no_energy):
        self.canvas = canvas
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.a = a
        self.hunger = hunger
        self.boredom = boredom
        self.no_energy = no_energy
        Critter2_.total += 1

    def talk(self):
        print("My name is", self.name, "and my mood is", self.mood())

    def eat(self,in_1):
        self.hunger -= in_1
        if self.hunger < 0:
            self.hunger = 0
        self.pass_time()

    def _sleep(self,x,y,sleep_ = 2):
            self.no_energy -= 2
            if self.no_energy < 0:
                self.no_energy = 0
            self.pass_time()
            canvas.create_oval(x+5,y+5,x+35,y+35,fill=self.color)
            root.update()
            time.sleep(5)
            canvas.delete("all")
            self.draw(x,y)

    def play(self,x,y,in_2):
        self.boredom -= in_2
        if self.boredom < 0:
            self.boredom = 0
        for i in range(4):
            canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
            canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
            canvas.create_oval(x+15,y+15,x+25,y+25,fill='black')
            root.update()
            time.sleep(0.25)
            canvas.delete("all")
            canvas.create_polygon(x+20,y+20-20*math.sqrt(2),x+20-20*math.sqrt(2),y+20,x+20,y+20+20*math.sqrt(2),x+20+20*math.sqrt(2),y+20,fill=self.color,outline="white")   
            canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
            canvas.create_oval(x+15,y+15,x+25,y+25,fill='black')
            root.update()
            time.sleep(0.25)
            canvas.delete("all")
            self.draw(x,y)

        self.pass_time()

    def mood(self):
        unhappiness = self.hunger + self.boredom + self.no_energy
        if unhappiness < 8:
            m = "прекрасно"
        elif 8 <= unhappiness <= 16:
            m = "неплохо"
        elif 17 <= unhappiness <= 24:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def pass_time(self):
        self.hunger += 1
        self.boredom += 1  
        self.no_energy += 1      

    def __str__(self):
        ans = 'Объект класса Critter\n' 
        ans += 'name: ' + self.name + '\n'
        return ans      
    
    def draw(self,x,y):
        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black')      

    def move(self,canvas,a,x,y,d):
        if a != "0":
            while 10 < x < 450 and 10 < y < 450: 
                if a == "R":
                    for i in range(d):
                        x += 2
                        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                        root.update()
                        time.sleep(0.05)
                        canvas.delete("all")   
                    break      
                elif a == "L":
                    for i in range(d):
                        x -= 2
                        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                        root.update()
                        time.sleep(0.05)
                        canvas.delete("all")
                    break   
                elif a == "U":
                    for i in range(d):
                        y -= 2
                        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                        root.update()
                        time.sleep(0.05)
                        canvas.delete("all")
                    break   
                elif a == "D":
                    for i in range(d): 
                        y += 2
                        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black')
                        root.update()
                        time.sleep(0.05)
                        canvas.delete("all")
                    break            
                elif a == "UR":
                    for i in range(d):
                        x += 2 
                        y -= 2
                        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                        root.update()
                        time.sleep(0.05)
                        canvas.delete("all")  
                    break     
                elif a == "UL":
                    for i in range(d):
                        x -= 2
                        y -= 2
                        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                        root.update()
                        time.sleep(0.05)
                        canvas.delete("all")
                    break      
                elif a == "DR": 
                    for i in range(d): 
                        x += 2
                        y += 2
                        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                        root.update()
                        time.sleep(0.05)
                        canvas.delete("all") 
                    break        
                elif a == "DL":
                    for i in range(d):
                        x -= 2
                        y += 2
                        canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                        canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                        canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                        root.update()
                        time.sleep(0.05)
                        canvas.delete("all") 
                    break
                self.pass_time()              

root = Tk()
canvas = Canvas(root,width=500,height=500,bg='black')
canvas.pack() 

def xy1(c1,xa,ya):
    de = 50
    dd = 50
    df = 50
    dg = 50
    a = "R"
    c1.move(canvas,a,xa,ya,de)
    if a == "R":
        xa += de*2
    if a == "L":
        xa -= de*2
    if a == "U":
        ya -= de*2
    if a == "D":
        ya += de*2
    if a == "UR":
        xa += de*2
        ya -= de*2
    if a == "UL":
        xa -= de*2
        ya -= de*2
    if a == "DR":
        xa += de*2
        ya += de*2
    if a == "DL":
        xa -= de*2
        ya += de*2    
    a = "D"
    c1.move(canvas,a,xa,ya,dd)
    if a == "R":
        xa += dd*2
    if a == "L":
        xa -= dd*2
    if a == "U":
        ya -= dd*2
    if a == "D":
        ya += dd*2
    if a == "UR":
        xa += dd*2
        ya -= dd*2
    if a == "UL":
        xa -= dd*2
        ya -= dd*2
    if a == "DR":
        xa += dd*2
        ya += dd*2
    if a == "DL":
        xa -= dd*2
        ya += dd*2 
    a = "L"
    c1.move(canvas,a,xa,ya,df)
    if a == "R":
        xa += df*2
    if a == "L":
        xa -= df*2
    if a == "U":
        ya -= df*2
    if a == "D":
        ya += df*2
    if a == "UR":
        xa += df*2
        ya -= df*2
    if a == "UL":
        xa -= df*2
        ya -= df*2
    if a == "DR":
        xa += df*2
        ya += df*2
    if a == "DL":
        xa -= df*2
        ya += df*2    
    a = "U"
    c1.move(canvas,a,xa,ya,dg)
    if a == "R":
        xa += dg*2
    if a == "L":
        xa -= dg*2
    if a == "U":
        ya -= dg*2
    if a == "D":
        ya += dg*2
    if a == "UR":
        xa += dg*2
        ya -= dg*2
    if a == "UL":
        xa -= dg*2
        ya -= dg*2
    if a == "DR":
        xa += dg*2
        ya += dg*2
    if a == "DL":
        xa -= dg*2
        ya += dg*2 
    c1.draw(xa,ya)
    in_1 = int(input())
    in_2 = int(input())
    c1.talk()
    c1.eat(in_1)
    c1.play(xa,ya,in_2)
    c1._sleep(xa,ya)

def main():
    c = "#" + ('%06x'%random.randint(0,16777215))
    c_1a = "#" + ('%06x'%random.randint(0,16777215))
    h_ = random.randint(0,10)
    b_ = random.randint(0,10)
    en_ = random.randint(0,10)
    hi_ = random.randint(0,10)
    bi_ = random.randint(0,10)
    eni_ = random.randint(0,10)
    xa = random.randint(10,450)
    ya = random.randint(10,450)
    xb = random.randint(10,450)
    yb = random.randint(10,450)
    c1 = Critter2_('First',c,xa,ya,canvas,"R",50,h_,b_,en_)
    c1.talk()
    c1.draw(xa,ya)
    xy1(c1,xa,ya)
    next_ = str(input())
    if next_ == "2":
        c2 = Critter2_('Second',c_1a,xb,yb,canvas,"L",50,hi_,bi_,eni_)
        c2.talk()
        c2.draw(xb,yb)
        c2.move(canvas,"L",xb,yb,50)
        Critter2_.status()
    root.update()
    time.sleep(1)

main()
root.mainloop()