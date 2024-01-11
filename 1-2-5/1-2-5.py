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

apple = Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()

score_write = Turtle()
score_write.penup()
score_write.goto(-440,340)



def travel():
    global score
    head.forward(speed)
    if abs(head.xcor() - apple.xcor()) < 10:
        if abs(head.ycor() - apple.ycor()) < 10:
            move_apple()
            score += 1
            score_write.clear()
            score_write.write(score, font=("Arial", 55, "bold"))
    if abs(head.xcor()) > 460:
        game_over()
    if abs(head.ycor()) > 360:
        game_over()
    wn.ontimer(travel, 10)

def move_apple():
    global speed
    loop = 0
    apple.goto(rand.randint(-300,300),rand.randint(-300,300))
    loop += 1
    if loop == 5:
        speed += 1
        loop = 0



def game_over():
    global final_message
    global score
    apple.hideturtle()
    head.hideturtle()
    score_write.clear()
    score_write.goto(-200,0)
    score_write.write("GAME OVER", font=("Arial", 55, "bold"))
    score_write.goto(-200,-55)
    score_write.write("FINAL SCORE:",font=("Arial", 55, "bold"))
    score_write.goto(-50, -110)
    score_write.write(score,font=("Arial", 55, "bold"))
    head.goto(0,0)

wn.onkey(lambda: head.left(90), 'Left')
wn.onkey(lambda: head.right(90), 'Right')


wn.listen()

travel()
move_apple()

wn.mainloop()