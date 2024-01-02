import turtle as trtl
import random as rand

wn = trtl.Screen()
wall = trtl.Turtle()

#Wall variables
wall_spacing = 20
wall_color = "peru"
wall_num = 7
distance_before_door = 0
distance_before_wall = 0
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
    global distance_before_door
    for border in range(3):
        wall.penup()
        wall.left(90)
        wall.forward(wall_length+10)
        wall_length += 20
        wall.pendown()
    for border in range(22):
        wall.left(90)
        door_wall_num = rand.randint(1,2)
        if door_wall_num == 1:
            draw_door(wall_length)
            make_wall(wall_length)
        if door_wall_num == 2:
            make_wall(wall_length)
            draw_door(wall_length)
        wall.forward(wall_length - (wall_spacing * 2) - distance_before_door - distance_before_wall + 40)
        wall_length += 20

def draw_door(wall_length):
    global distance_before_door
    distance_before_door = rand.randint((wall_spacing * 2), wall_length - (wall_spacing * 2))
    wall.forward(distance_before_door)
    wall.penup()
    wall.forward(wall_spacing * 2)
    wall.pendown()


def make_wall(wall_length):
    global distance_before_wall
    distance_before_wall = rand.randint((wall_spacing * 2), wall_length - (wall_spacing * 2))
    wall.forward(distance_before_wall)
    wall.left(90)
    wall.forward(wall_spacing * 2)
    wall.back(wall_spacing * 2)
    wall.right(90)

make_maze(20)
wn.mainloop()
