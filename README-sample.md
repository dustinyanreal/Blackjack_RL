# Dynamic Pricing for Highway Priority Lanes 
## Project Summary
<!-- Around 200 Words -->
<!-- Cover (1) What problem you are solving, (2) Who will use this RL module and be happy with the learning, and (3) a brief description of the results -->
Traffic congestion poses a significant societal challenge with substantial economic repercussions. We propose a dynamic pricing system for entry to highway priority lanes. These lanes allow drivers to bypass traffic by paying a fee, but pricing can be a delicate balance. If too costly, demand plummets, and if too cheap, the priority lanes lose their purpose. Our solution involves implementing an intelligent agent that continually adjusts the pricing structure based on the congestion status of highways.

We model users by considering their individual price thresholds, accommodating their preferences and financial abilities. Vehicles entering and exiting the highways follow statistical distribution patterns, such as Poisson arrival process. By employing this approach, we demonstrate how dynamic pricing can guarantee the appropriate flow of traffic, while simultaneously generating extra revenue. This innovation represents a vital step towards mitigating traffic congestion and its associated economic impacts, enhancing the overall quality of transportation services in urban environments.

## State Space
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

We assume an RL agent is placed for each segment of highway and decides the price to enter the priority lane within the segment based on the congestion level.

The congestion level is defined by the average speed simulated in the environment based on the number of vehicles in the segment.

| Num | Observation                                         | Min | Max |
|-----|-----------------------------------------------------|-----|-----|
| 0   | Average speed of vehicles (overall congestion level)        | 0   | 150 |
| 1   | Average speed of vehicles in the priority lane (priority lane congestion level)        | 0   | 150 |
| 2   | Average percentage of vehicles in the priority lane | 0   | 100 |
| 3   | Current price to enter the priority lane            | 0   | 10  |

## Action Space
The RL agent decide the price to enter the priority lane.
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->
| Num | Observation                                         | Min | Max |
|-----|-----------------------------------------------------|-----|-----|
| 0   | Price to enter the priority lane        | 0   | 10 |


## Rewards
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

When the average speed of vehicles in the priority lane becomes less than 50 miles/hour, the agent receives a penalty of -10 * (the number of vehicles in the priority lane). Otherwise, it receives a positive reward based on the total revenue per vehicle in the priority lane.


## RL Algorithm 
We use PPO. Briefly explain the category such as off-policy, policy gradient-based approach... Cite a paper.

We are going to use the ray rllib implementation. Describe important parameters and configurations.


## Starting State [if applicable]
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->
This is a continuing task.

## Episode End [if applicable]
<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->
This is a continuing task.

## Results
- Explain main results
- Show the plot of increasing returns over time
- Show a few extra plots to highlight the benefits of the RL approach (e.g. earned revenue compared with a random pricing method, the probability of the average speed of vehicles in the priority lane reaching less than 50 miles/hour)

# Blackjack Agent to Maximize reward(money)!
## Project Summary
In the world of gambling, blackjack is a very popular card game. We propose an agent that can try and beat the casino by earning a lot of reward(money). The game is mostly luck, but with a bit a statistics, the odds for a person to beat the casino becoming slightly higher.

The dealer/casino will have a simple strategy of just hitting(getting more cards) until it reaches either a number that is greater than 21, or until it reaches a number that we consider a valid stopping point. For a valid stopping point for a dealer/casino, it will stop when its cards add up to x, where 17 <= x >= 21. We also define that if a dealer gets a soft 17 i.e (A,6), the dealer will also stop. 

For the agent, we will have it randomly pick options: Double, Hit, Stand, Split. It will learn when to stop or when to hit, but if it reaches a number greater than 21, the agent losses. The agent will also have a little bit of a tricky strategy where it will count cards and understand the propabilities of potential cards to pop up. With "coutning cards", the agent will pick it's actions accordingly.

## State Space
Simplified:
    The Game will have already started, and the cards will be dealt one by one, updating "counting cards", 

    | Num | Observation                                         | Min | Max |
    |-----|-----------------------------------------------------|-----|-----|

