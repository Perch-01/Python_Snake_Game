from turtle import Screen, _Screen, Turtle
from constants import DM


class ScoreBoard(Turtle):
    def __init__(self, screen: _Screen):
        super().__init__()

        self.score = 0
        self.screen = screen
        self.writeText(f'Score: {self.score}')

    def increaseScore(self):
        self.score += 1
        self.writeText(f'Score: {self.score}')

    def writeText(self, to_write: str):
        self.reset()
        self.penup()
        self.goto((0, (DM/2)-60))
        self.color('white')
        self.hideturtle()
        style = ('Courier', 13, 'normal')
        self.write(to_write, font=style, align='center')


    def resetScore(self):
        self.score = 0
        self.writeText(f'Score: {self.score}')
