import turtle as trtl

wn = trtl.Screen()
wall = trtl.Turtle()

#Wall variables
wall_spacing = 20
wall_color = "peru"
wall_num = 7
#wall_length = 20
start_x = 0
start_y = 0
wall_thick = 5

#Wall Properties
wall.pensize(wall_thick)
wall.speed(0)
wall.pencolor(wall_color)

def goto_start():
    wall.penup()
    wall.goto(start_x, start_y)
    wall.pendown()

#Set up maze
def setup_maze(wall_length):
    global wall_spacing
    for border in range(25):
        wall.left(90)
        wall.forward(wall_length)
        wall_length += wall_spacing
def make_doors(wall_length):
    global wall_spacing
    for border in range(25):
        wall.left(90)
        wall.forward(10)
        wall.penup()
        wall.forward(wall_spacing*2)
        wall.pendown()
        wall.forward(wall_length - 30)
        wall_length += wall_spacing


make_doors(20)
wn.mainloop()