import matplotlib.pyplot as plt

def plot_signals(data, signals, title='Buy and Sell Signals'):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Price', color='blue', alpha=0.5)
    plt.plot(data.loc[signals == 1].index, 
             data['Close'][signals == 1], 
             '^', markersize=10, color='g', label='Buy Signal')
    plt.plot(data.loc[signals == -1].index, 
             data['Close'][signals == -1], 
             'v', markersize=10, color='r', label='Sell Signal')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def plot_returns(data, title='Cumulative Returns of the Strategy'):
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Cumulative_Strategy_Returns'], label='Cumulative Returns', color='purple')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()