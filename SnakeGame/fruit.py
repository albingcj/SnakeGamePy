from turtle import Turtle
import random
class Fruit(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rx = random.randint(-240, 240)
        ry = random.randint(-240, 240)
        self.goto(rx, ry)

