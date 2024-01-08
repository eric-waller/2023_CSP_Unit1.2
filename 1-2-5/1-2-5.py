from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor('green')

head = Turtle()
head.color('black')
head.penup()

speed = 1

def travel():
    head.forward(speed)
    wn.ontimer(travel, 10)

wn.onkey(lambda: head.setheading(90), 'Up')
wn.onkey(lambda: head.setheading(180), 'Left')
wn.onkey(lambda: head.setheading(0), 'Right')
wn.onkey(lambda: head.setheading(270), 'Down')

wn.listen()

travel()

wn.mainloop()