import gymnasium as gym
from gymnasium import ObservationWrapper
import numpy as np

class CustomObservationWrapper(ObservationWrapper):
    
    def __init__(self, env : gym.Env , goal = "microwave"):
        super(CustomObservationWrapper ,self).__init__(env)
        env_model = env.env.env.env.model
        env_model.opt.gravity[:] = np.array([0.0, 0.0, -1])
        self.goal = goal

    def set_goal(self, goal):
        self.goal = goal

    def reset(self):
        state, info = self.env.reset()
        observation = self.process_observation(state)
        return observation, info

    def step(self, action):
        state, reward, terminated, truncated, info = self.env.step(action)
        observation = self.process_observation(state)
        return observation, reward, terminated, truncated, info
    

    def process_observation(self, observation):
        obs_position = observation['observation']
        obs_achieved_goal = observation['achieved_goal']
        obs_desired_goal = observation['desired_goal']

        #concatenate the observations
        #shape: (obs_position + obs_achieved_goal + obs_desired_goal)
        obs_concat = np.concatenate([obs_position, obs_achieved_goal[self.goal], obs_desired_goal[self.goal]])

    
        