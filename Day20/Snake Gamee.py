import time
from turtle import Screen, Turtle, back, width
from Create import Snake
from food import Food
from ScoreBoard import ScoreBoard
screen=Screen()
snake=Snake()
food=Food()
screen.title("Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
game_is_on=True
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
screen.onkey(snake.down,"s")
score=ScoreBoard()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        game_is_on=False
        score.game_over()
    for snk in snake.snakes:
        if snk == snake.head:
            pass
        elif snake.head.distance(snk)<10:
            game_is_on=False
            score.game_over()
screen.exitonclick()