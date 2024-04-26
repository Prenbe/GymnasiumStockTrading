# Import necessary packages
import gym
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gymnasium as gym

# Define the stock trading environment
class SimpleTradingEnv(gym.Env):
    """A simple stock trading environment for educational purposes"""
    metadata = {'render.modes': ['human']}

    def __init__(self, df):
        super(SimpleTradingEnv, self).__init__()
        self.df = df
        self.reward_range = (-np.inf, np.inf)
        # Actions: 0 = Hold, 1 = Buy, 2 = Sell
        self.action_space = gym.spaces.Discrete(3)
        # Normalize observation space for all stock data columns
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(len(df.columns),), dtype=np.float32)
        self.reset()

    def _next_observation(self):
        # Normalize the observation to be between 0 and 1
        normalized_data = (self.df.iloc[self.current_step] - self.df.min()) / (self.df.max() - self.df.min())
        return normalized_data.values

    def step(self, action):
        # Implement the logic to handle actions and update the portfolio value
        current_price = self.df.loc[self.current_step, 'Close']
        if action == 1:  # Buy
            self.shares_held = self.current_portfolio_value // current_price
            self.current_portfolio_value %= current_price
        elif action == 2 and self.shares_held > 0:  # Sell
            self.current_portfolio_value += self.shares_held * current_price
            self.shares_held = 0
        self.current_step += 1
        if self.current_step >= len(self.df) - 1:
            self.done = True
        self.reward = self.current_portfolio_value  # Simplified reward calculation
        return self._next_observation(), self.reward, self.done, {}

    def reset(self):
        # Reset the environment to an initial state
        self.current_step = 0
        self.current_portfolio_value = 10000  # Reset to initial portfolio value
        self.shares_held = 0
        self.done = False
        return self._next_observation()

    def render(self, mode='human'):
        # Plot the closing prices along with the short-term and long-term SMAs
        plt.figure(figsize=(10, 5))
        plt.plot(self.df['Close'], label='Close Price')
        plt.plot(self.df['short_sma'], label='20-day SMA')
        plt.plot(self.df['long_sma'], label='50-day SMA')
        plt.legend()
        plt.show()

# Load and preprocess stock data
def load_data(filename):
    df = pd.read_csv(filename)
    df['short_sma'] = df['Close'].rolling(window=20).mean()
    df['long_sma'] = df['Close'].rolling(window=50).mean()
    return df

# Main function to run the environment
def main():
    df = load_data('FAANG_Stock_Data.csv')
    env = SimpleTradingEnv(df)
    state = env.reset()
    done = False

    while not done:
        # Implement a decision strategy based on SMA crossover
        short_sma = df.loc[env.current_step, 'short_sma']
        long_sma = df.loc[env.current_step, 'long_sma']
        action = 0  # Default to hold
        if short_sma > long_sma:
            action = 1  # Buy
        elif short_sma < long_sma:
            action = 2  # Sell
        state, reward, done, info = env.step(action)
        if done:
            break

    env.render()
    print(f"Final portfolio value: ${env.current_portfolio_value:.2f}")

if __name__ == '__main__':
    main()
