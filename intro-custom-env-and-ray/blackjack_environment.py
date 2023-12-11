import numpy as np
import pygame
from typing import Optional
from numpy import random

import gymnasium as gym
from gymnasium import spaces

original_deck = [1,1,1,1, #A
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

def check_shuffle():
    shuffle = False
    if (len(deck) < int(len(original_deck)/2)):
        if len(deck) <= (len(original_deck) * 1/4):
            shuffle = True
        else:
            x = random.randint(100)
            if x > 75:
                shuffle = True
    return shuffle

def compare(a, b):
    return float(a > b) - float(a < b)

def draw_card(np_random):
    card = int(np_random.choice(deck))
    deck.remove(card)
    #shuffle = check_shuffle()
    return card #shuffle

def draw_hand(np_random):
    card1 = int(np_random.choice(deck))
    deck.remove(card1)
    card2 = int(np_random.choice(deck))
    deck.remove(card2)
    #shuffle = check_shuffle()
    return [card1, card2] #, shuffle

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

class BlackJackEnv(gym.Env):
    def __init__(self, natural=False):

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Tuple(
            (spaces.Discrete(32), spaces.Discrete(11), spaces.Discrete(2))
        )
        self.natural = natural

    def step(self, action):
        #shuffle_next_turn = False
        terminated = False
        assert self.action_space.contains(action)
        if is_blackjack(self.player):
            action = 1
        if action == 2: #double
            terminated = True
            card = draw_card(self.np_random)
            #if shuffle:
            #    shuffle_next_turn = True
            self.player.append(card)
            if is_bust(self.player):
                reward = -2.0
            else:
                while sum_hand(self.dealer) < 17:
                    card = draw_card(self.np_random)
                    #if shuffle:
                    #    shuffle_next_turn = True
                    self.dealer.append(card)
                reward = compare(score(self.player), score(self.dealer))
                reward *= 2
        elif action == 1: #hit
            card = draw_card(self.np_random)
            #if shuffle:
            #    shuffle_next_turn = True
            self.player.append(card)
            if is_bust(self.player):
                terminated = True
                reward = -1.0
            else:
                terminated = False
                reward = 0.0
        elif action == 0: #stand
            terminated = True
            while sum_hand(self.dealer) < 17:
                card = draw_card(self.np_random)
                #if shuffle:
                #    shuffle_next_turn = True
                self.dealer.append(card)
            reward = compare(score(self.player), score(self.dealer))
            if is_blackjack(self.player) and is_blackjack(self.dealer):
                reward = 0.0
            elif is_blackjack(self.player) and not is_blackjack(self.dealer):
                reward = 1.5

        if terminated:
            if check_shuffle():
                deck = original_deck

        return self._get_obs(), reward, terminated, False, {}

    def _get_obs(self):
        return (sum_hand(self.player), self.dealer[0], is_ace(self.player))
    
    def reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None):
        super().reset(seed=seed)
        self.dealer = draw_hand(self.np_random)
        self.player = draw_hand(self.np_random)

        _, dealer_card_value, _ = self._get_obs()

        #deck = original_deck

        return self._get_obs(), {}
