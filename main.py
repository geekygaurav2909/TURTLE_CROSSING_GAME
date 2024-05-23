from turtle import Screen
from turtle_movement import MainTurtle
from enemies import Enemies
from score import Scoreboard
import time

screen = Screen()
screen.title("!!The Turtle Crossing Game!!")
screen.setup(width=600,height=600)
screen.tracer(0)

turtle = MainTurtle()
enemy = Enemies()
score = Scoreboard()

# Control the Hero Turtle
screen.listen()
screen.onkeypress(turtle.move_up,"Up")
screen.onkeypress(turtle.move_down,"Down")
screen.onkeypress(turtle.move_left,"Left")
screen.onkeypress(turtle.move_right,"Right")


is_game_on = True
looper = 0

while is_game_on:
    looper +=1

    time.sleep(score.timer)

    enemy.constant_flow()

    screen.update()

    # Detect collision with enemy.
    for hitting_head in enemy.enemies_list:
        if turtle.distance(hitting_head) <30:
            is_game_on =False
            turtle.enemy_hit() 


    # Detect collision with wall.
    if (turtle.xcor() > 260 
        or turtle.xcor() < -260  
        or turtle.ycor() < -260
        ):
        is_game_on = False
        turtle.game_over()


    # Reset the position, once turtle reaches the top.
    if turtle.ycor() > 240:
        score.update()
        turtle.goto(turtle.initial_pos)


    if looper%25 == 0:
        enemy.enemy_gang()

screen.exitonclick()