from turtle import Turtle

MOVE = 10
MY_FONT = ("Impact", 22, "normal")

class MainTurtle(Turtle):

    def __init__(self, shape: str = "turtle"):
        super().__init__(shape)
        self.penup()
        self.initial_pos = (0,-260)
        self.color("black","yellow")
        self.shapesize(1.5,1.5)
        self.goto(self.initial_pos)
        self.setheading(90)


    def move_up(self):
        current_x = self.xcor()
        new_y = self.ycor() + MOVE
        self.goto(current_x,new_y)


    def move_down(self):
        current_x = self.xcor()
        new_y = self.ycor() - MOVE
        self.goto(current_x,new_y)


    def move_left(self):
        current_y = self.ycor()
        new_x = self.xcor() - MOVE
        self.goto(new_x,current_y)


    def move_right(self):
        current_y = self.ycor()
        new_x = self.xcor() + MOVE
        self.goto(new_x,current_y)


    def game_over(self):
        self.goto(0,0)
        self.ht()
        self.write("You have crossed the window. Game Over!", align="center", font= MY_FONT)

    def enemy_hit(self):
        self.goto(0,0)
        self.ht()
        self.write("You have collided with enemy. Game Over!", align="center", font= MY_FONT)