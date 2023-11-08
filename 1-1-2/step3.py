# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
bob = trtl.Turtle()
turt_color = "pink"


#-----initialize turtle-----
bob.shape("turtle")
bob.pencolor(turt_color)
bob.fillcolor(turt_color)

#-----game functions--------
def bob_clicked(x, y):
    print("You caught bob")
def change_position(x, y):
    newxpos = rand.randint(-400,400)
    newypos = rand.randint(-300, 300)
    bob.penup()
    bob.goto(newxpos, newypos)
    bob.pendown()
score = 0


#-----events----------------
bob.onclick(change_position)
wn = trtl.Screen()
wn.mainloop()