import yfinance as yf
import datetime
import pandas as pd
from math import pow, sqrt

#stocks = ['SPY', 'QQQ', 'XLK', 'XLC', 'XLY', 'XLE', 'XLF', 'XLI', 'XLP', 'XLU', 'XLV']
stocks = ['GOOG']
for stock in stocks:
    ticker = yf.Ticker(stock)
    name = ticker.info['longName']
    # repair=True causes yfinance to adjust for dividends and splits that weren't in the adjusted close price
    end = datetime.date(2022, 12, 2)
    start = datetime.date(2020, 12, 2)
    data = ticker.history(start=start, end=end, interval='1mo', repair=True)
    print(data['Close'])
    data['Monthly Return'] = data['Close'].pct_change()
    #print(type(data['Monthly Return']))
    num_months = len(data['Monthly Return'][1:])
    yearly_returns = []
    for value in data['Monthly Return'][1:]:
        yearly_returns.append(pow((1+value), 12) - 1)
    upside_potential = 0.0
    downside_risk = 0.0
    for yearly_return in yearly_returns:
        value = yearly_return - 0.08
        if (value > 0):
            upside_potential += value
        else:
            downside_risk += value*value
    upside_potential = upside_potential/num_months
    downside_risk = sqrt(downside_risk/(num_months-1))
    tpr = upside_potential/downside_risk
    print(stock, name, upside_potential, downside_risk, tpr)

    out = pd.DataFrame(data['Monthly Return'])
    out.to_csv('out.csv')
