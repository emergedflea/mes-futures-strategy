# mes-futures-strategy

## Overview
This project implements a simple long/short trading strategy for the Micro E-mini S&P 500 (MES) futures using various technical indicators. The strategy aims to capitalize on market movements by executing trades based on signals generated from these indicators.

## Project Structure
```
mes-futures-strategy
├── src
│   ├── main.py                # Entry point of the application
│   ├── strategy
│   │   └── long_short.py      # Contains the LongShortStrategy class
│   ├── indicators
│   │   └── moving_average.py   # Functions to calculate moving averages
│   ├── data
│   │   └── loader.py          # Loads historical price data
│   └── utils
│       └── helpers.py         # Utility functions for the project
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation for the project
└── .gitignore                 # Files to ignore in version control
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd mes-futures-strategy
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have access to historical price data for the Micro E-mini S&P 500 futures.

## Usage
To run the trading strategy, execute the following command:
```
python src/main.py
```

This will initialize the trading strategy, load the necessary data, and execute trades based on the defined indicators.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.