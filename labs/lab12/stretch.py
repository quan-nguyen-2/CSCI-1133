import turtle
import random

class Shape:

    def __init__(self, x=0, y=0, color = "000000"):
        self.x = x
        self.y = y
        self.color = color
        self.fill = False

    def set_fill_color(self, color):
        self.color = color

    def set_filled(self, y_or_n):
        self.filled = y_or_n

    def is_filled(self):
        if self.filled:
            return True
        return False

class Circle(Shape):

    def __init__(self, x=0, y=0,radius =1, color = "000000"):
        Shape.__init__(self, x, y, color)
        self.radius = radius
    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()

        print(self.is_filled())
        if self.is_filled():
            t.fillcolor(self.color)
            t.begin_fill()
            t.circle(self.radius)
            t.end_fill()
        else:
            t.circle(self.radius)

class Rectangle:


class Display:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.elements = []
        self.turtle.speed(0)
        self.screen.delay(0)
        self.turtle.hideturtle()
        self.screen.onclick(self.mouse_event)

    def mouse_event(self, x, y):
        color_lst = ["blue", "red", "yellow", "purple", "orange", "green"]
        random.shuffle(color_lst)
        final_circle = Circle(x, y, random.randint(10, 100), color_lst[0])
        final_circle.set_filled(True)
        final_circle.draw(self.turtle)

    def add(self, shape):
        self.elements.append(shape)
        shape.draw(self.turtle)
        

game = Display()
turtle.done()
