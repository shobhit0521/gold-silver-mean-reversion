import pandas as pd
import numpy as np

class MeanReversionStrategy:
    def __init__(self, data, window=20, entry_threshold=1.0, exit_threshold=0.0):
        self.data = data
        self.window = window
        self.entry_threshold = entry_threshold
        self.exit_threshold = exit_threshold
        self.signals = pd.Series(index=self.data.index, data=0)

    def generate_signals(self):
        rolling_mean = self.data['Close'].rolling(window=self.window).mean()
        rolling_std = self.data['Close'].rolling(window=self.window).std()
        
        z_score = (self.data['Close'] - rolling_mean) / rolling_std
        
        # Generate buy/sell signals
        self.signals[z_score < -self.entry_threshold] = 1  # Buy signal
        self.signals[z_score > self.entry_threshold] = -1  # Sell signal
        self.signals[(z_score >= -self.exit_threshold) & (z_score <= self.exit_threshold)] = 0  # Exit signal

    def calculate_returns(self):
        self.data['Signal'] = self.signals.shift()
        self.data['Daily_Return'] = self.data['Close'].pct_change()
        self.data['Strategy_Return'] = self.data['Daily_Return'] * self.data['Signal']
        self.data['Cumulative_Strategy_Return'] = (1 + self.data['Strategy_Return']).cumprod() - 1
        return self.data[['Cumulative_Strategy_Return']]