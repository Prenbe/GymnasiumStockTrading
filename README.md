# Simple Stock Trading Environment

This project uses Python and the Gymnasium library to simulate a stock trading environment. Students are expected to complete specific tasks within the code to implement a basic trading strategy using historical stock data.

## Project Objective
Implement a simple stock trading environment using the SMA crossover strategy for buy and sell signals.

### Data
This file (FAANG_Stock_Data.csv) contains daily data points including opening and closing prices, highs and lows, and volume of traded stocks from the past three months for the following organizations:
Amazon
Netflix
Apple
Google
Meta
This data is from Yahoo Finance.

## Understanding Simple Moving Average (SMA)
The Simple Moving Average (SMA) is a technical indicator used to smooth out price data by creating a constantly updated average price. The SMA is calculated by taking the arithmetic mean of a given set of values over a specific number of periods. In stock trading, SMAs can help identify trends and reversals by comparing short-term averages to long-term averages.

### How the SMA Crossover Strategy Works
Buy Signal: This occurs when the short-term SMA crosses above the long-term SMA, suggesting an upward trend and a potential buying opportunity.
Sell Signal: This occurs when the short-term SMA crosses below the long-term SMA, indicating a downward trend and a potential selling point.

### Implementation in the Project
Students will implement two SMAs in their project:
Short-term SMA (20 days): This reflects more recent market movements.
Long-term SMA (50 days): This shows a more extended market trend.

## Tasks
1. **Load and Preprocess Data**:
   - Load historical stock data and calculate two moving averages: a short-term SMA (20 days) and a long-term SMA (50 days).
   
2. **Implement the Trading Logic**:
   - Modify the `step` method to implement trading decisions based on the SMA crossover strategy:
     - If the short-term SMA is above the long-term SMA, consider it a buy signal.
     - If the short-term SMA is below the long-term SMA, consider it a sell signal.
     - Implement logic to handle buying if not currently holding stocks and selling if stocks are held.

3. **Reset and Render Methods**:
   - Ensure the environment can be reset to its initial state after each episode.
   - Implement a `render` method to visualize the stock prices along with the short-term and long-term SMAs.

## Hints
- Use `pandas` rolling and mean functions to calculate moving averages.
- Use logical conditions to set the `action` based on SMA comparisons.
- Ensure portfolio updates are correctly applied based on the action taken.

### Packages Used

- `gym`: Provides the basic environment classes and methods necessary for creating custom environments for simulations.
- `numpy`: Used for numerical operations on arrays and matrices.
- `pandas`: Essential for data manipulation and analysis, particularly useful for handling time-series data.
- `matplotlib.pyplot`: Used for creating static, interactive, and animated visualizations in Python.

### Key Functions and Methods

- `gym.spaces.Discrete`: Provides a discrete space of possible actions (e.g., buy, sell, hold).
- `gym.spaces.Box`: Defines an n-dimensional box space for observations, used to specify the shape and bounds of the observation data.
- `pandas.read_csv()`: Reads data from a CSV file into a DataFrame, which is ideal for handling structured data.
- `pandas.DataFrame.iloc`: Purely integer-location based indexing for selection by position in DataFrame.
- `matplotlib.pyplot.plot()`: Plots y versus x as lines and/or markers.
- `matplotlib.pyplot.figure()`: Creates a new figure.
- `matplotlib.pyplot.show()`: Displays all open figures.

## Example of Fill-in-the-Blanks
I've provided a sample code document titled trading_env_student where the student can fill-in-the-blank in various sections of the code. I've also provided trading_env_answers that could be used to give students steps and/or hints if they get stuck or need additional guidance.
