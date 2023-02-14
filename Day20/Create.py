starting_position=[(0,0),(-20,0),(-40,0)]
move_distance=20
Up=90
Down=-90
Left=180
Right=0
from turtle import Turtle
class Snake:
    def __init__(self):
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]
    def create_snake(self):
        for position in starting_position:
            self.add_tail(position)
    def add_tail(self, position):
        snake=Turtle()
        snake.color("White")
        snake.shape("circle")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)
    def move(self):
        for snke_num in range(len(self.snakes)-1,0,-1):
            new_x=self.snakes[snke_num-1].xcor()
            new_y=self.snakes[snke_num-1].ycor()
            self.snakes[snke_num].goto(new_x,new_y)
        self.snakes[0].forward(move_distance)
    def extend(self):
        self.add_tail(self.snakes[-1].position())
    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)
    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)
    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)