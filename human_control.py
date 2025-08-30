import gymnasium as gym
import gymnasium_robotics
import numpy as np
from gym_robotics_custom import CustomObservationWrapper

if __name__ == "__main__":

    env_name="FrankaKitchen-v1"
    max_episodes_steps = 500

    task = "microwave" 
    task_no_spaces = task.replace(" ", "_")

    gym.register_envs(gymnasium_robotics) 

    # Create environment
    env = gym.make(
                    env_name, 
                    max_episode_steps=max_episodes_steps, 
                    tasks_to_complete=[task],
                    render_mode="human"
                )

    env = CustomObservationWrapper(env , goal = task)

    print(env.env.env.env.env.model.opt.gravity)
    
    # Reset environment
    # state, info = env.reset()
    # print(f"State: {state}")

    # env.close()
    
    