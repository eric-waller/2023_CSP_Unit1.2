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
def make_maze(wall_length):
    global wall_spacing
    for border in range(3):
        wall.penup()
        wall.left(90)
        wall.forward(wall_length+10)
        wall_length += 20
        wall.pendown()
    for border in range(21):
        wall.left(90)
        draw_door()
        make_wall()
        wall.forward(wall_length - 10 - (wall_spacing * 2))
        wall_length += 20

def draw_door():
    wall.forward(10)
    wall.penup()
    wall.forward(wall_spacing * 2)
    wall.pendown()


def make_wall():
    wall.forward(40)
    wall.left(90)
    wall.forward(wall_spacing * 2)
    wall.back(wall_spacing * 2)
    wall.right(90)

make_maze(20)
wn.mainloop()
