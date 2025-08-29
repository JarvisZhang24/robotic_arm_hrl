import gymnasium as gym
import gymnasium_robotics
import numpy as np

if __name__ == "__main__":

    env_name="FrankaKitchen-v1"
    max_episodes_steps = 500
    task = "microwave" 

    gym.register_envs(gymnasium_robotics) 

    # Create environment
    env = gym.make(
                    env_name, 
                    max_episode_steps=max_episodes_steps, 
                    tasks_to_complete=[task],
                    render_mode="human"
                )
    
    # Reset environment
    state, info = env.reset()
    print(f"State: {state}")
    
    