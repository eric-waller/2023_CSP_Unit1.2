#   a123_apple_1.py
import random
import turtle as trtl


#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

letterlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
  draw_letter()

def change_apple_location(apple):
  random_xcoord_increase = random.randint(0, 250)
  random_xcoord_decrease = random.randint(0, 250)
  apple.penup()
  apple.goto(random_xcoord_increase - random_xcoord_decrease, 0)
  apple.pendown()

def draw_letter():
  global  random_letter
  random_letter = random.randint(0,25)
  wn.tracer(False)
  apple.color("black")
  drawing_xcord = apple.xcor()
  drawing_ycord = apple.ycor()
  apple.penup()
  apple.goto(drawing_xcord - 21, drawing_ycord - 45)
  apple.write(letterlist[random_letter], font=("Arial", 55, "bold"))
  apple.goto(drawing_xcord, drawing_ycord)
  apple.pendown()
  wn.tracer(True)

def apple_fall():
  global apple
  apple.shape(apple_image)
  xcoord = apple.xcor()
  ycoord = apple.ycor()
  fall_coord = ycoord - 175
  apple.penup()
  apple.goto(xcoord, fall_coord)
  apple.clear()
  apple.hideturtle()




#-----function calls-----
draw_apple(apple)

wn.onkeypress(apple_fall, letterlist[random_letter])
wn.bgpic("background.gif")
wn.listen()
wn.mainloop()