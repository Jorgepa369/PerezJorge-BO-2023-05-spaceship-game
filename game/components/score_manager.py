import pygame

class ScoreManager:
    def __init__(self):
        self.death_counter = 0
        self.score = 0
        self.highest_score_list = []
        self.highest_score = 0

    def death_count(self):
        self.death_counter += 1

    def update_score(self):
        self.score += 1
        return self.score
    def score_list(self, score):
        self.highest_score_list.append(score)

    def high_score(self):
        if len(self.highest_score_list) > 1:
            self.highest_score = max(self.highest_score_list)
        else:
            self.highest_score = self.score
        return self.highest_score