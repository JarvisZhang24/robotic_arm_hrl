import gymnasium as gym
from gymnasium import ObservationWrapper
import numpy as np

class CustomObservationWrapper(ObservationWrapper):
    
    def __init__(self, env : gym.Env , goal = "microwave"):
        super(CustomObservationWrapper ,self).__init__(env)
        env_model = env.env.env.env.model
        env_model.opt.gravity[:] = np.array([0.0, 0.0, -1])