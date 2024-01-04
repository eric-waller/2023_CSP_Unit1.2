import turtle as trtl
import random as rand

wn = trtl.Screen()

snake_body = []

#setup snake
head = trtl.Turtle()
head.shape("triangle")

#setup apple
apple = trtl.Turtle()


def turnleft():
    head.left(90)
def turnright():

wn.onkeypress(turn)
wn.mainloop()