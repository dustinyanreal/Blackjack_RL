import numpy as np
import pygame

import gymnasium as gym
from gymnasium import spaces

deck = [1,1,1,1,
        2,2,2,2,
        3,3,3,3,
        4,4,4,4,
        5,5,5,5,
        6,6,6,6,
        7,7,7,7,
        8,8,8,8,
        9,9,9,9,
        10,10,10,10, #10
        10,10,10,10, #J
        10,10,10,10, #Q
        10,10,10,10] #K

def check_if_win(a, b):
    return float(a > b) - float(a < b)

def draw_card(np_random):
    card = int(np_random.choice(deck))
    return card

def draw_hand(np_random):
    card1 = int(np_random.choice(deck))
    card2 = int(np_random.choice(deck))
    return [card1, card2]

def is_ace(hand):
    return 1 in hand and sum(hand) + 10 <= 21

def sum_hand(hand):
    if is_ace(hand):
        return sum(hand) + 10
    return sum(hand)

def is_bust(hand):
    return sum_hand(hand) > 21

def score(hand):
    return 0 if is_bust(hand) else sum_hand(hand)

def is_blackjack(hand):
    return sorted(hand) == [1, 10]

class BlackJackEnv():
    def __init__(self, natural=False):

        self.action_space = spaces.Discrete(3)
        self.observatuib_space = spaces.Tuple(
            (spaces.Discrete(32), spaces.Discrete(11), spaces.Discrete(2))
        )
        self.natural = natural

    def step(self, action):
        assert self.action_space.contains(action)
        if action == 2: #double
            terminated = True
            self.player.append(draw_card(self.np_random))
            if is_bust(self.player):
                reward = -2.0
            else:
                while sum_hand(self.dealer) < 17:
                    self.dealer.append(draw_card(self.np_random))
                reward = check_if_win(score(self.player), score(self.dealer))
                reward *= 2
        elif action == 1: #hit
            self.player.append(draw_card(self.np_random))
            if is_bust(self.player):
                reward = -1.0
            else:
                terminated = False
                reward = 0.0
        elif action == 0: #stand
            terminated = True
            while sum_hand(self.dealer) < 17:
                self.dealer.append(draw_card(self.np_random))
            reward = check_if_win(score(self.player), score(self.dealer))
        else: #blackjack
            reward = 1.5

    def __get_obs(self):
        return (sum_hand(self.player), self.dealer[0], is_ace(self.player))
    
    def reset(self):
        self.dealer = draw_hand(self.np_random)
        self.player = draw_hand(self.np_random)
