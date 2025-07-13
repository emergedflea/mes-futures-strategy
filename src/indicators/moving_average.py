def calculate_moving_average(data, window):
    if len(data) < window:
        raise ValueError("Data length must be greater than or equal to the window size.")
    
    moving_averages = []
    for i in range(len(data) - window + 1):
        window_data = data[i:i + window]
        moving_average = sum(window_data) / window
        moving_averages.append(moving_average)
    
    return moving_averages