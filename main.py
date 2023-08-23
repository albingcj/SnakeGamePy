import time
from turtle import Screen
from snake import sn
from fruit import Fruit
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.tracer(0)

sn = sn()
fr = Fruit()
sc = Score()


screen.listen()
screen.onkey(sn.up, "Up")
screen.onkey(sn.down, "Down")
screen.onkey(sn.left, "Left")
screen.onkey(sn.right, "Right")

on = True
while on:
    screen.update()
    time.sleep(0.1)
    sn.move()
    if sn.head.distance(fr) < 15:
        fr.refresh()
        sn.extend()
        sc.increase()

    if sn.head.xcor() > 250 or sn.head.ycor() > 250 or sn.head.xcor() < -250 or sn.head.ycor()< -250:
        sn.head.goto(-sn.head.xcor(), -sn.head.ycor())
        # on = False
        # sc.gameover()
    for x in sn.seg:
        if x == sn.head:
            pass
        elif sn.head.distance(x) < 10:
            on = False
            sc.gameover()
screen.exitonclick()
