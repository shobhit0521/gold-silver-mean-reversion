import pandas as pd

def run_backtest(signals, historical_data):
    """
    Run backtest for the mean reversion strategy.

    Parameters:
    signals (pd.Series): Series containing buy/sell signals.
    historical_data (pd.DataFrame): DataFrame containing historical price data.

    Returns:
    pd.DataFrame: DataFrame containing the backtest results.
    """
    # Initialize a DataFrame to hold the backtest results
    results = pd.DataFrame(index=historical_data.index)
    
    # Calculate daily returns
    historical_data['Returns'] = historical_data['Close'].pct_change()
    
    # Create a column for strategy returns
    results['Strategy_Returns'] = signals.shift(1) * historical_data['Returns']
    
    # Calculate cumulative returns
    results['Cumulative_Strategy_Returns'] = (1 + results['Strategy_Returns']).cumprod()
    results['Cumulative_Market_Returns'] = (1 + historical_data['Returns']).cumprod()
    
    return results