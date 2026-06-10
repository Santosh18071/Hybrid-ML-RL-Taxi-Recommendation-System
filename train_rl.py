from stable_baselines3 import PPO
from rl_environment import TaxiEnv

env = TaxiEnv()

model = PPO(
    "MlpPolicy",
    env,
    verbose=1
)

model.learn(
    total_timesteps=5000
)

model.save(
    "ppo_model"
)