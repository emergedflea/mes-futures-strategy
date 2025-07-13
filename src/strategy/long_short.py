class LongShortStrategy:
    def __init__(self, data, short_window, long_window):
        self.data = data
        self.short_window = short_window
        self.long_window = long_window
        self.signals = None

    def calculate_signals(self):
        self.data['short_mavg'] = self.data['close'].rolling(window=self.short_window, min_periods=1).mean()
        self.data['long_mavg'] = self.data['close'].rolling(window=self.long_window, min_periods=1).mean()
        self.data['signals'] = 0
        self.data['signals'][self.short_window:] = np.where(
            self.data['short_mavg'][self.short_window:] > self.data['long_mavg'][self.short_window:], 1, 0
        )
        self.signals = self.data['signals']

    def execute_long(self):
        if self.signals.iloc[-1] == 1:
            print("Executing Long Trade")
            # Logic for executing a long trade goes here

    def execute_short(self):
        if self.signals.iloc[-1] == 0:
            print("Executing Short Trade")
            # Logic for executing a short trade goes here

    def run_strategy(self):
        self.calculate_signals()
        self.execute_long()
        self.execute_short()