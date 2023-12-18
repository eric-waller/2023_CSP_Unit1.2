#   a123_apple_1.py
import turtle as trtl
import random as rand

# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
drawer = trtl.Turtle()

wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file
wn.addshape(pear_image)  # Make the screen aware of the new file
apple_letter_x_offset = 25
apple_letter_y_offset = 50
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

apple = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()
apple.penup()
wn.tracer(False)

letter = "a"
# -----functions-----
def draw_apple(active_apple, letter):
    active_apple.showturtle()
    active_apple.shape(apple_image)
    drawLetter(active_apple, letter)
    wn.update()


def drawLetter(active_apple, letter):
    drawer.penup()
    drawer.goto(active_apple.xcor() - apple_letter_x_offset, active_apple.ycor() - apple_letter_y_offset)
    drawer.color("white")
    drawer.clear()
    drawer.write(letter, font=("Arial", 55, "bold"))

def reset_apple(active_apple):
    if letter_list:
        global letter
        letter = rand.choice(letter_list)
        letter_list.remove(letter)
        active_apple.goto(rand.randint(-270, 270), 160)
        print(letter_list)
        draw_apple(active_apple, letter)

def drop_apple():
    wn.tracer(True)
    apple.goto(apple.xcor(), apple.ycor() - 400)
    apple.hideturtle()
    wn.tracer(False)
    reset_apple(apple)

def check_a():
    global letter
    if letter == "a":
        drop_apple()
def check_b():
    global letter
    if letter == "b":
        drop_apple()
def check_c():
    global letter
    if letter == "c":
        drop_apple()
def check_d():
    global letter
    if letter == "d":
        drop_apple()
def check_e():
    global letter
    if letter == "e":
        drop_apple()
def check_f():
    global letter
    if letter == "f":
        drop_apple()
def check_g():
    global letter
    if letter == "g":
        drop_apple()
def check_h():
    global letter
    if letter == "h":
        drop_apple()
def check_i():
    global letter
    if letter == "i":
        drop_apple()
def check_j():
    global letter
    if letter == "j":
        drop_apple()
def check_k():
    global letter
    if letter == "k":
        drop_apple()
def check_l():
    global letter
    if letter == "l":
        drop_apple()
def check_m():
    global letter
    if letter == "m":
        drop_apple()
def check_n():
    global letter
    if letter == "n":
        drop_apple()
def check_o():
    global letter
    if letter == "o":
        drop_apple()
def check_p():
    global letter
    if letter == "p":
        drop_apple()
def check_q():
    global letter
    if letter == "q":
        drop_apple()
def check_r():
    global letter
    if letter == "r":
        drop_apple()
def check_s():
    global letter
    if letter == "s":
        drop_apple()
def check_t():
    global letter
    if letter == "t":
        drop_apple()
def check_u():
    global letter
    if letter == "u":
        drop_apple()
def check_v():
    global letter
    if letter == "v":
        drop_apple()
def check_w():
    global letter
    if letter == "w":
        drop_apple()
def check_x():
    global letter
    if letter == "x":
        drop_apple()
def check_y():
    global letter
    if letter == "y":
        drop_apple()
def check_z():
    global letter
    if letter == "z":
        drop_apple()

# -----function calls-----
draw_apple(apple, "A")
wn.onkeypress(check_a, "a")
wn.onkeypress(check_b, "b")
wn.onkeypress(check_c, "c")
wn.onkeypress(check_d, "d")
wn.onkeypress(check_e, "e")
wn.onkeypress(check_f, "f")
wn.onkeypress(check_g, "g")
wn.onkeypress(check_h, "h")
wn.onkeypress(check_i, "i")
wn.onkeypress(check_j, "j")
wn.onkeypress(check_k, "k")
wn.onkeypress(check_l, "l")
wn.onkeypress(check_m, "m")
wn.onkeypress(check_n, "n")
wn.onkeypress(check_o, "o")
wn.onkeypress(check_p, "p")
wn.onkeypress(check_q, "q")
wn.onkeypress(check_r, "r")
wn.onkeypress(check_s, "s")
wn.onkeypress(check_t, "t")
wn.onkeypress(check_u, "u")
wn.onkeypress(check_v, "v")
wn.onkeypress(check_w, "w")
wn.onkeypress(check_x, "x")
wn.onkeypress(check_y, "y")
wn.onkeypress(check_z, "z")

wn.listen()
wn.bgpic("background.gif")
wn.mainloop()