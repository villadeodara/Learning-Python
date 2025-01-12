import yfinance as yf
import pandas as pd
from math import pow, sqrt
import datetime
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Compute yearly return from monthly return by extrapolating to 12 months.
def compute_yearly_return(monthly_return):
    return pd.Series(((1 + monthly_return.to_numpy())**12 - 1),
                     index=monthly_return.index)

# Compute TPR from the yearly return array.
def compute_one_tpr(yearly_return, dtr):
    zeros = pd.Series(np.zeros(len(yearly_return)), index=yearly_return.index)
    upside_return = (zeros + yearly_return[yearly_return > dtr] - dtr).fillna(0)
    downside_return = (zeros + yearly_return[yearly_return < dtr] - dtr).fillna(0)
    upside_potential = upside_return.mean()
    downside_risk = sqrt((downside_return * downside_return).mean())
    tpr = upside_potential/downside_risk
    return tpr

# Compute TPR for the give yearly return series, dtr, and a span. It will use the returns of
# (span - 1 ) previous months and the current month to compute the tpr of the current month.
# Returns the tpr series. The output series's lenght is (span-1) shorter than the input.
def compute_tpr_series(yearly_return, dtr, span):
    if (len(yearly_return) < span):
        raise ValueError("Not enough data in yearly return")
    index = yearly_return.index[span - 1 :]
    tpr_array = []
    for i in range(span - 1, len(yearly_return)):
        tpr = compute_one_tpr(yearly_return[i - span + 1 : i + 1], dtr)
        tpr_array.append(tpr)
    return pd.Series(tpr_array, index=index)

def plot(tpr_df, plot_file):
    plt.figure()
    tpr_df.plot(xlabel='Date', ylabel='TPR')
    plt.savefig(plot_file)

def table_output(tpr_df, table_file):
    with open(table_file, "w") as file:
        file.write(tpr_df.to_markdown())


def main():
    # yearly desired target return
    dtr = 0.08
    # compute tpr from 6 previous months and this month
    span = 7

    end = datetime.date(2024, 12, 2)
    start = datetime.date(2005, 12, 2)

    #stocks = ['SPY', 'QQQ', 'XLK', 'XLC', 'XLY', 'XLE', 'XLF', 'XLI', 'XLP', 'XLU', 'XLV']
    stocks = ['GOOG', 'META', 'CSCO', 'MSFT', 'AMZN', 'AAPL']
    tpr_dict = {}
    for stock in stocks:
        ticker = yf.Ticker(stock)
        # repair=True causes yfinance to adjust for dividends and splits that weren't in the adjusted close price
        data = ticker.history(start=start, end=end, interval='1mo', repair=True)
        monthly_return = data['Close'].pct_change().dropna()
        yearly_return = compute_yearly_return(monthly_return)
        tpr_series = compute_tpr_series(yearly_return, dtr, span)
        tpr_dict[stock] = tpr_series
    tpr_df = pd.DataFrame(tpr_dict)
    print(tpr_df)
    plot(tpr_df, "tpr_plot.pdf")
    table_output(tpr_df, "tpr_table.txt")

if __name__ == "__main__":
    main()

