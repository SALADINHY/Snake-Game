from pickle import TRUE
from turtle import Screen, Turtle, color, shape, width
import heroes
import random
colors=["red","blue","pink","yellow","gray"]
y_position=[-100,-70,-40,-10,20]
all_turtle=[]
#jimmy= Turtle()
#timmy.shape("turtle")
#timmy.color("red")
#jimmy.shape("turtle")
#jimmy.color("blue")
#colors=["red","blue","yellow","gray","pink","purple"]
#def mf():
#    timmy.forward(20)
#def bw():
#    timmy.back(20)
#def l():
#    newhead=timmy.heading()+10
#    timmy.setheading(newhead)
#def r():
#    newhead=timmy.heading()-10
#    timmy.setheading(newhead)
#def clear():
#    timmy.clear()
#    timmy.penup()
#    timmy.home()
#    timmy.pendown()
screen=Screen()
#screen.listen()

#screen.onkey(mf,"w")
#screen.onkey(bw,"s")
#screen.onkey(l,"a")
#screen.onkey(r,"d")
#screen.onkey(clear,"c")
screen.setup(width=500,height=400)
for addturtle in range(0,5):
    tim=Turtle(shape="turtle")
    tim.color(colors[addturtle])
    tim.penup()
    tim.goto(x=-230,y=y_position[addturtle])
    all_turtle.append(tim)
race_on= True
while race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            race_on= False
            winning=turtle.pencolor()
            print(f"Color winning is {winning}")
        go=random.randint(0,10)
        turtle.forward(go)
screen.exitonclick()
