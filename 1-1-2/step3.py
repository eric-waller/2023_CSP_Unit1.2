# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
leaderboard_file_name = "leaderboard.txt"
player_name = input("Name:")

bob = trtl.Turtle()
score_writer = trtl.Turtle()
turt_color = "pink"

score = 0
font_setup = "Arial", 20, "normal"

timer = 5
counter_interval = 1000
timer_up = False
#-----initialize turtle-----
bob.shape("turtle")
bob.pencolor(turt_color)
bob.fillcolor(turt_color)
counter = trtl.Turtle()
#Score turt command
score_writer.penup()
score_writer.goto(-400, -350)
score_writer.pendown()

#Counter turt command
counter.penup()
counter.goto(-400, 350)

#-----game functions--------
def updateScore():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def bob_clicked():
    print(score)


def change_position(x, y):
    newxpos = rand.randint(-400,400)
    newypos = rand.randint(-300, 300)
    bob.penup()
    bob.goto(newxpos, newypos)
    bob.pendown()
    updateScore()
    bob_clicked()

def countdown():
  global timer
  global timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    bob.hideturtle()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

#-----events----------------
bob.onclick(change_position)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()