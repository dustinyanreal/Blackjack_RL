# Project Name
## Project Summary
<!-- Around 200 Words -->
<!-- Cover (1) What problem you are solving, (2) Who will use this RL module and be happy with the learning, and (3) a brief description of the results -->
In the world of gambling, blackjack is a very popular card game. We propose an agent that can try and beat the casino by earning a lot of reward(money). The game is mostly luck, but with a bit a statistics, the odds for a person to beat the casino becoming slightly higher.

The dealer/casino will have a simple strategy of just hitting(getting more cards) until it reaches either a number that is greater than 21, or until it reaches a number that we consider a valid stopping point. For a valid stopping point for a dealer/casino, it will stop when its cards add up to x, where 17 <= x >= 21. We also define that if a dealer gets a soft 17 i.e (A,6), the dealer will continue.

For the agent, we will have it randomly pick options: Double, Hit, Stand. It will learn when to stop or when to hit, but if it reaches a number greater than 21, the agent losses. The agent will also have a little bit of a tricky strategy where it will count cards and understand the propabilities of potential cards to pop up. With "coutning cards", the agent will pick it's actions accordingly.

If you're an passionate blackjack player and want an Agent to count cards and find the best move to play to earn a lot of money! Then this is the module for you!

## State Space
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->
The observation space will consists of a 3-tuple containing: the player's current sum, the value of the dealer's one showing card (1-10 where 1 is an ace), and whether the player holds a usuable ace(0,1)

## Action Space
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->
The action space will indicate the action the player takes. There are 3 options that a player can take.

    0: stand
    1: hit
    2: double

## Rewards
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->
Since the goal of blackjack is to beat the dealer by getting close to 21, we will have 3 normal rewards and add 2 extra rewards for the double action.

If we don't double:
    +1.0 if we beat the dealer
    0 if we go even with the dealer
    -1.0 if we lose to the dealer
If we double:
    +2.0 if we beat the dealer
    0 if we go even with the dealer <!-- The same as wehn we don't double -->
    -2.0 if we lose to the dealer

## RL Algorithm 

## Starting State [if applicable]
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->
The starting state will depend on what the player has and what the dealer can see.
    For a player, we can see the 32 different states it can achive.
    For a dealer, we will see 10 states
    and we will also have a state for ACES to see if they are usable.

## Episode End [if applicable]
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->
For this environment, we will end the episode if one of the followin occur:
    1. If we have -100 as our reward, we don't want to lose too much money!
    2. If the episode length is greater than 500, we don't want to sit at a blackjack table forever!

## Results
The results I recieved were not what I wanted. When I ran my environment without any sort of training, My results were bad. The reward at the end was always negative. Close to the amount of steps I ran.
When I trained an agent with PPO (Proximal Policy Optimization), I saw a huge increase in performance. Training on 200 different episodes and running my agent with the same amount of steps 200, I saw that the cumulative reward sum to a negative number closer to 0. My cumulative reward averaged around -5, which is really good to compared to -100. With more training, I could see the agent averaging +5-10.

Since training takes too long for my device I wasn't able to run many tests to see if I could achieve what I wanted.

