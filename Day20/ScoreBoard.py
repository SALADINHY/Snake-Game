from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_board()
    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_board()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",24,"normal"))
    def update_board(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))