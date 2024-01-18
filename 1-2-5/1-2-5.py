from turtle import Turtle, Screen
import random as rand

wn = Screen()
wn.bgcolor('green')

head = Turtle()
head.color('black')
head.penup()
head.shapesize(2)

speed = 5

score = -1
color_list = ["red", "orange", "yellow"]
apple = Turtle()
apple.shapesize(2)
apple.shape("circle")
apple.color("red")
apple.penup()

score_write = Turtle()
score_write.penup()
score_write.goto(-440, 340)
color_list_len = 2


def travel():
    global score
    global speed
    head.forward(speed)
    print(speed)
    if abs(head.xcor() - apple.xcor()) < 20:
        if abs(head.ycor() - apple.ycor()) < 20:
            move_apple()
            score += 1
            score_write.clear()
            score_write.write(score, font=("Arial", 55, "bold"))
            speed += score/8
    if abs(head.xcor()) > 460:
        game_over()
    if abs(head.ycor()) > 390:
        game_over()
    wn.ontimer(travel, 10)


def move_apple():
    global speed
    global color_list_len
    global score
    loop = 0
    apple.goto(rand.randint(-300, 300), rand.randint(-300, 300))
    if score == 10:
        color_list.append("blue")
        color_list_len += 1
    if score == 15:
        color_list.append("purple")
        color_list_len += 1
    if score == 25:
        color_list.append("white")
        color_list_len += 1
    color_num = rand.randint(0, color_list_len)
    apple.color(color_list[color_num])
    loop += 1
    if loop == 2:
        speed += 5
        loop -= 2


def game_over():
    global score
    if score >= 10:
        if score < 15:
            score_write.color("blue")
    if score >= 15:
        if score < 25:
            score_write.color("purple")
    if score >= 25:
        score_write.color("white")
    apple.hideturtle()
    head.hideturtle()
    score_write.clear()
    score_write.goto(-200, 0)
    score_write.write("GAME OVER", font=("Arial", 55, "bold"))
    score_write.goto(-200, -55)
    score_write.write("FINAL SCORE:", font=("Arial", 55, "bold"))
    score_write.goto(-50, -110)
    score_write.write(score, font=("Arial", 55, "bold"))
    head.goto(0, 0)


wn.onkey(lambda: head.left(90), 'Left')
wn.onkey(lambda: head.right(90), 'Right')


wn.listen()

travel()
move_apple()

wn.mainloop()
