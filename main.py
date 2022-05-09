import turtle, random
from random import randint

class Turtle_Shapes(object):
    def __init__(self, x):
        self.x = x

    #Shape generator.
    def generator(self):
        turtle.pensize(4)
        l = 100 #Length.
        a = 360 #Angle.
        colors = ["green","blue", "red", "black", "yellow", "gray"] #Color selection.
        turtle.penup()
        turtle.goto(randint(-300,0),randint(0,300)) #Random start.
        for i in range(3, 11):
            turtle.pendown()
            rcolor = random.choice(colors)
            turtle.pencolor(rcolor)
            for j in range(0, i):
                turtle.forward(l)
                turtle.right(a/i)
    
    #Multiple objects.
    def times(self):
        for _ in range(self.x):
            self.generator()
        turtle.done()

x = int(input("# of Shapes: "))
ts = Turtle_Shapes(x)
ts.times()