import turtle as trtl
import random as rand

wn = trtl.Screen()
wall = trtl.Turtle()

#Wall variables
path_width = 20
wall_color = "peru"
wall_num = 7
rainbow_maze_list = ["red","orange red","dark orange","orange","gold","yellow","green yellow","lawn green","spring green","medium spring green","dark turquoise", "royal blue", "medium slate blue", "blue violet", "dark orchid","medium violet red","crimson" ]
color_num = 0
#wall_length = 20
start_x = 0
start_y = 0
wall_thick = 10

#Wall Properties
wall.pensize(wall_thick)
wall.speed(0)
wall.pencolor(rainbow_maze_list[color_num])

def goto_start():
    wall.penup()
    wall.goto(start_x, start_y)
    wall.pendown()

#Set up maze
def make_maze(wall_length):
    global path_width
    global color_num
    for border in range(25):
        if border < 4:
            wall.penup()
            wall.left(90)
            wall.forward(wall_length+10)
            wall_length += 20
            wall.pendown()
        else:
            wall.left(90)
            door_wall_num = rand.randint(1,2)
            if door_wall_num == 1:
                draw_door()
                make_wall()
            if door_wall_num == 2:
                make_wall()
                draw_door()
            wall.forward(wall_length - 10 - (path_width * 2))
            wall_length += 20
            wall.pencolor(rainbow_maze_list[color_num])
            if color_num > 15:
                color_num = 0
            else:
                color_num += 1

def draw_door():
    wall.forward(10)
    wall.penup()
    wall.forward(path_width * 2)
    wall.pendown()


def make_wall():
    wall.forward(40)
    wall.left(90)
    wall.forward(path_width * 2)
    wall.back(path_width * 2)
    wall.right(90)

make_maze(10)
wn.mainloop()
