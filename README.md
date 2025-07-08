<<<<<<< HEAD
# Gold and Silver Mean Reversion Strategy

This project implements a mean reverting trading strategy for Gold and Silver ETFs. The strategy is based on the principle that prices tend to revert to their historical mean over time. 

## Project Structure

- **data/**: Contains historical price data for Gold and Silver ETFs.
  - `goldbees_4yr_data.csv`: Historical price data for the GoldBees ETF over the last four years.
  - `hdfcgold_4yr_data.csv`: Historical price data for the HDFC Gold ETF over the last four years.
  - `nippon_silver_4yr_data.csv`: Historical price data for the Nippon Silver ETF over the last four years.
  - `gold_silver_inr_4yr_data.csv`: Historical price data for gold and silver in INR over the last four years.

- **notebooks/**: Contains Jupyter notebooks for analysis and strategy implementation.
  - `mean_reversion_strategy.ipynb`: Implements the mean reversion strategy for Gold and Silver ETFs, including data analysis, strategy implementation, and visualization of results.

- **src/**: Contains source code for data loading, strategy implementation, backtesting, and plotting.
  - `data_loader.py`: Functions to load and preprocess historical price data from CSV files.
  - `strategy.py`: Implements the mean reversion strategy with methods to generate buy/sell signals and calculate returns.
  - `backtest.py`: Contains the backtesting logic for the mean reversion strategy.
  - `plot_utils.py`: Utility functions for plotting results.

- **requirements.txt**: Lists the required Python packages for the project, such as pandas, numpy, matplotlib, and yfinance.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gold-silver-mean-reversion
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Jupyter notebook to analyze the mean reversion strategy:
   ```
   jupyter notebook notebooks/mean_reversion_strategy.ipynb
   ```

## Usage

- Load the historical price data using the functions in `data_loader.py`.
- Implement the mean reversion strategy using the `MeanReversionStrategy` class in `strategy.py`.
- Backtest the strategy using the `run_backtest` function in `backtest.py`.
- Visualize the results using the plotting functions in `plot_utils.py`.

## License

This project is licensed under the MIT License.
=======
# gold-silver-mean-reversion
>>>>>>> 7894e59b76bb36bacf01378d27ae139b7a9a252b
