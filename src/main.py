# src/main.py

from data.loader import load_data
from strategy.long_short import LongShortStrategy

def main():
    # Load historical price data for the Micro E-mini S&P 500 futures
    data = load_data()

    # Initialize the trading strategy
    strategy = LongShortStrategy(data)

    # Execute the long/short strategy
    strategy.execute_long()
    strategy.execute_short()

if __name__ == "__main__":
    main()