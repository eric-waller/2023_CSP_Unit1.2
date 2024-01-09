from turtle import Turtle, Screen
import random as rand

wn = Screen()
wn.bgcolor('green')

head = Turtle()
head.color('black')
head.penup()

speed = 2

score = 0

apple = Turtle()
apple.shape("circle")
apple.color("red")

head_x = head.xcor()
head_y = head.ycor()

apple_xval = 0
apple_yval = 0

def travel():
    head.forward(speed)
    wn.ontimer(travel, 10)

def apple_move():
    global apple_xval
    global apple_yval
    apple_xval = rand.randint(-200,200)
    apple_yval = rand.randint(-200,200)
    apple.goto(apple_xval,apple_yval)


if (apple_xval - head_x) < 20:
    apple_move()
    score += 1


wn.onkey(lambda: head.left(90), 'Left')
wn.onkey(lambda: head.right(90), 'Right')


wn.listen()

travel()


wn.mainloop()