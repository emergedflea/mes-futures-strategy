def load_data(file_path):
    import pandas as pd

    # Load historical price data for Micro E-mini S&P 500 futures
    data = pd.read_csv(file_path)

    # Preprocess and format the data as needed
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    return data

def preprocess_data(data):
    # Implement any additional preprocessing steps here
    return data