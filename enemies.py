from turtle import Turtle
import random

# colormode(255)
MOVING_SPEED = 10
FIX_XAXIS = 280
ENEMIES_POS = [-220,-140,-60,20,100,180,230]
SPEED = [1,5,8,11,15,19,25]
COLOR_LIST = ['red','yellow','blue','green','black','purple','orange']


class Enemies:

    def __init__(self):
        self.enemies_list = []
        self.enemy_gang()


    def enemy_gang(self):
        for y_axis in ENEMIES_POS:
            new_enemy = Turtle("turtle")
            new_enemy.penup()
            new_enemy.color(random.choice(COLOR_LIST))
            new_enemy.shapesize(1.5,1.5)
            new_enemy.goto(FIX_XAXIS,y_axis)
            new_enemy.setheading(180)
            self.enemies_list.append(new_enemy)


    def constant_flow(self):
        for enemy_lead in self.enemies_list:
            enemy_lead.fd(random.choice(SPEED))

   




