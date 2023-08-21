from turtle import Turtle
S = [(0, 0), (-20, 0), (-40, 0)]
U = 90
D = 270
L = 180
R = 0
po = 20
class sn:
    def __init__(self):
        self.seg = []
        self.create()
        self.head = self.seg[0]

    def create(self):
        for p in S:
            self.addex(p)

    def addex(self, po):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(po)
        self.seg.append(tim)

    def extend(self):
        self.addex(self.seg[-1].position())


    def move(self):
        for x in range(len(self.seg)-1, 0, -1):
            self.seg[x].goto(self.seg[x-1].pos())
        self.head.forward(po)

    def up(self):
        if self.head.heading() != D:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != U:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != R:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != L:
            self.head.setheading(0)