import gymnasium as gym
from blackjack_environment import BlackJackEnv
import ray
from ray import tune, train
from ray.rllib.algorithms import ppo
from ray.tune.registry import register_env
from ray.rllib.algorithms.ppo import PPOConfig


#Register the environment
gym.register(
    id='Blackjackdustin-v0',
    entry_point='blackjack_environment:BlackJackEnv',
    max_episode_steps=500,
)

env = gym.make('Blackjackdustin-v0')

ray.init()
algo = ppo.PPO(env=BlackJackEnv, config={
    "env_config": {},  # config to pass to env class
})


for i in range(250):
    print(i)
    algo.train()

state, _ = env.reset()
sum_rewards = 0

for i in range(200):
    action = algo.compute_single_action(state)
    state, reward, terminated, _, _, = env.step(action)
    sum_rewards += reward

    if terminated:
        print("cumulative reward: ", sum_rewards)
        state, _ = env.reset()
