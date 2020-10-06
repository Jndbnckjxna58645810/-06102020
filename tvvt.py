import random
from tkinter import *
class TV_TV():
    def __init__(self,battery,v):
        self.battery = battery
        self.v = v
    def energy(self):
        self.battery -= 1
        return self.battery
    def volume(self):
        vi = int(input("vi"))
        if 0 <= vi <= 100:
            self.v = vi
            print("The volume is",self.v)
class TVchannel():
    def __init__(self,number,ca2,co2,canvas,a_):
        self.number = number
        self.ca2 = ca2
        self.co2 = co2
        self.canvas = canvas
        self.a_ = a_
    def draw(self):
        canvas.create_rectangle(10,10,490,490,fill=self.ca2,outline="white")
        if 0 <= self.a_ < 25:
            canvas.create_rectangle(225,225,275,275,fill=self.co2,outline="white")
        elif 25 <= self.a_ < 50:
            canvas.create_oval(225,225,275,275,fill=self.co2,outline="white")  
        elif 50 <= self.a_ < 75:
            canvas.create_line(10,10,490,490,fill="white")
            canvas.create_rectangle(225,225,275,275,fill=self.co2,outline="white")
        elif 75 <= self.a_ < 100:
            canvas.create_line(10,490,490,10,fill="white")
            canvas.create_rectangle(225,225,275,275,fill=self.co2,outline="white") 
        elif 100 <= self.a_ < 125:
            canvas.create_line(10,10,490,490,fill="white")
            canvas.create_oval(225,225,275,275,fill=self.co2,outline="white")
        elif 125 <= self.a_ <= 150:
            canvas.create_line(10,490,490,10,fill="white")
            canvas.create_oval(225,225,275,275,fill=self.co2,outline="white") 
        print("You are watching ",self.number)         
root = Tk()
canvas = Canvas(root,width=500,height=500,bg='black')
canvas.pack() 
def main():
    m = int(input("m"))
    t_v = TV_TV(100,50)
    channels = dict()
    for i in range(m):
        ca2 = "#" + ('%06x'%random.randint(0,16777215))
        co2 = "#" + ('%06x'%random.randint(0,16777215))
        a_ = random.randint(0,150)
        channels[i] = TVchannel(i,ca2,co2,canvas,a_)
    while t_v.energy != 0:
        p = int(input("p"))
        if p == 0:
            i = int(input("i"))
            channels[i].draw()
            continue
        elif p == 1:
            t_v.volume()
        elif p == 2:
            print(t_v.energy())
    else:
        canvas.delete("all")
main()
root.mainloop()