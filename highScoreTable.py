# 15th Sept 24 
# https://www.codewars.com/kata/5962bbea6878a381ed000036/train/python

class HighScoreTable: 

    def __init__(self, size):
        self.size = size  
        self.scores = [] 

    def update(self, score):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        if len(self.scores) > self.size: 
            self.scores.pop()

    def reset(self):
        self.scores = []  

    