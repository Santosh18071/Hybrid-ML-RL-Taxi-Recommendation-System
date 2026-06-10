import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TaxiEnv(gym.Env):

    def __init__(self):

        super().__init__()

        self.action_space = spaces.Discrete(5)

        self.observation_space = spaces.Box(
            low=0,
            high=100,
            shape=(4,),
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):

        state = np.random.rand(4).astype(np.float32)

        return state, {}

    def step(self, action):

        reward = np.random.rand()

        next_state = np.random.rand(4).astype(np.float32)

        terminated = False

        truncated = False

        return next_state, reward, terminated, truncated, {}
    