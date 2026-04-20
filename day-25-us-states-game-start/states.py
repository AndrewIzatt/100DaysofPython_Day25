import pandas as pd
from turtle import Turtle

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.states = pd.read_csv("./50_states.csv")

    def check_answer(self, answer):
        pass
        # if answer in self.states.Series