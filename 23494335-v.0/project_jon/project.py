import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import pi, exp, log, sqrt, ceil
import datetime

def calc_upr(mReturns, dtr):
  def erfc(x):
    z = abs(x)
    if z > 8:
      ans = 0
    else:
      t = 1.0 / (1.0 + 0.5 * z)
      a = t * 0.17087277
      a = t * (-0.82215223 + a)
      a = t * (1.48851587 + a)
      a = t * (-1.13520398 + a)
      a = t * (0.27886807 + a)
      a = t * (-0.18628806 + a)
      a = t * (0.09678418 + a)
      a = t * (0.37409196 + a)
      a = t * (1.00002368 + a)
      ans = t * exp(-z * z - 1.26551223 + a)
    if x >= 0:
      return ans
    else:
      return 2.0 - ans

  SQRT2 = 1.4142136

  # x is monthly returns; bootstrap annual returns
  numBoot = 10000
  yReturns = []
  for _ in range(numBoot):
    mReturn = np.random.choice(mReturns, size = 12, replace = True)
    yRet = np.prod(1 + mReturn)
    yReturns.append((yRet - 1) * 100)

  smean = np.mean(yReturns)
  ssdev = np.std(yReturns)
  smin = min(yReturns)
  smax = max(yReturns)

  # fit log-normal
#   shape, loc, scale = sp.stats.lognorm.fit(yreturns)					# can be unreliable

  # lognorm.fit uses pdf of the form:
  # (1 / [(x-loc) * sqrt(2*pi) * shape]) * exp(-log((x-loc) / scale)^2 / (2*shape^2))
  # traditional pdf is of the form:
  # (1 / [(x-tau) * sqrt(2*pi) * sigma]) * exp(-(log(x-tau) - mu)^2 / (2*sigma^2))
  #
  # (log(x-tau) - mu)^2 = log((x-loc) / scale)^2
  # log(x-tau) - mu = log((x-loc) / scale)
  # log(x-tau) - mu = log(x-loc) - log(scale)
  #
  # so tau = loc and mu = log(scale)

#   mu = log(scale)
#   sigma = shape
#   sigma2 = sigma ** 2
#   tau = loc
#
#   extremeIsMin = (mu - min(yreturns)) < (max(yreturns) - mu)

  # alternative: estimate parameters without resorting to lognorm.fit

  if (smean - smin) < (smax - smean):
    extremeIsMin = True
    tau = smin - 7 * ssdev
    delta = smean - tau
  else:
    extremeIsMin = False
    tau = smax + 7 * ssdev
    delta = tau - smean

  # if X is distributed as a 3-param lognorm, then:
  # E(X) = tau + exp(mu + sigma^2 / 2)
  # Var(X) = exp(2*mu + sigma^2) * (exp(sigma^2) - 1) = exp(mu + sigma^2 / 2)^2 * (exp(sigma^2) - 1) = (E(X) - tau)^2 * (exp(sigma^2) - 1)

  sigma2 = log(ssdev ** 2 / delta ** 2 + 1)
  mu = log(delta) - sigma2 / 2
  sigma = sqrt(sigma2)

  # downside probability
  if extremeIsMin:
    x = dtr - tau
    if x > 0:
      dp = 1 - 0.5 * erfc((log(x) - mu) / (SQRT2 * sigma))
    else:
      dp = 0
  else:
    x = tau - dtr
    if x > 0:
      dp = 0.5 * erfc((log(x) - mu) / (SQRT2 * sigma))
    else:
      dp = 1

  # upside potential
  if extremeIsMin:
    if dtr > tau:
      b = dtr - tau
      c = SQRT2 * sigma
      up = 0.5 * exp(mu + 0.5 * sigma2) * (2 - erfc((mu + sigma2 - log(b)) / c))
    else:
      up = tau + exp(mu + sigma2 / 2)
  else:
    if tau > dtr:
      b = tau - dtr
      c = SQRT2 * sigma
      up = 0.5 * exp(mu + 0.5 * sigma2) * ( erfc((mu + sigma2 - log(b)) / c) )
    else:
      up = 0
  if extremeIsMin and tau < dtr:
    up -= (dtr - tau) * (1 - dp)
  if not extremeIsMin and tau > dtr:
    up = (tau - dtr) * (1 - dp) - up

  # downside deviation
  if extremeIsMin:
    if dtr > tau:
      b = dtr - tau
      c = SQRT2 * sigma
      a = (log(b) - mu) / c
      dd = 0.5 * exp(2 * mu + 2 * sigma2) * (2 - erfc(a - c)) - b * (2 - erfc(a - c / 2)) * exp(mu + sigma2 / 2) + 0.5 * b ** 2 * (2 - erfc(a))
    else:
      dd = 0
  else:
    if tau > dtr:
      b = tau - dtr
      c = SQRT2 * sigma
      a = (log(b) - mu) / c
      dd = 0.5 * exp(2 * mu + 2 * sigma2) * erfc(a - c) - b * exp(mu + sigma2 / 2) * erfc(a - c / 2) + 0.5 * b ** 2 * erfc(a)
    else:
      m = tau - exp(mu + sigma2 / 2)
      v = (m - tau) ** 2 * (exp(sigma2) - 1)
      dd = v + (dtr - m) ** 2
  if dd < 0:
    dd = 0
  else:
    dd = sqrt(dd)

  # upside potential ratio
  upr = up / dd

  return upr, up, dd, yReturns, mu, sigma, tau, smean, ssdev, smin, smax, extremeIsMin

#

def lognormpdf(x, mu, sigma, tau, extremeIsMin):
  alpha = 1 / (sqrt(2 * pi) * sigma)
  beta = -1 / (2 * sigma ** 2)

  if extremeIsMin:
    return (alpha / (x - tau)) * exp(beta * (log(x - tau) - mu) ** 2)
  else:
    return (alpha / (tau - x)) * exp(beta * (log(tau - x) - mu) ** 2)

# parameters for analysis

dtr = 8
maxPortPct = 20
numYears = 5
stocks = ['SPY', 'QQQ', 'XLK', 'XLC', 'XLY', 'XLE', 'XLF', 'XLI', 'XLP', 'XLU', 'XLV']

#

numStocks = len(stocks)
if numStocks > 4:
  cols = 3
else:
  cols = 2
rows = ceil(numStocks / cols)
if numStocks > 1:
  fig, axs = plt.subplots(rows, cols, layout='constrained')
  fig.set_size_inches(3*cols, 3*rows)
  fig.suptitle(f'DTR={dtr:.2f}')

row = 0
col = 0
sum_upr = 0
n = 0
results = []
for stock in stocks:
  ticker = yf.Ticker(stock)
  name = ticker.info['longName']
  # repair=True causes yfinance to adjust for dividends and splits that weren't in the adjusted close price
  today = datetime.date(2023, 1, 1)
  data = ticker.history(start=today - datetime.timedelta(days=numYears*365), end=today, interval='1mo', repair=True)
  data['Return'] = data['Close'].pct_change()
  upr, up, dd, yReturns, mu, sigma, tau, smean, ssdev, smin, smax, extremeIsMin = calc_upr(data['Return'].dropna(), dtr)
  if upr > 1:
    sum_upr += upr
  results.append([name, dtr, upr, up, dd, 0])

  xAxis = np.linspace(min(yReturns), max(yReturns), num=100)
  if numStocks == 1:
    ax = plt.gca()
  elif rows == 1:
    ax = axs[col]
  else:
    ax = axs[row, col]

  if numStocks == 1:
    ax.set_title(f'{stock} (UPR={upr:.2f}, DTR={dtr:.2f})')
  else:
    ax.set_title(f'{stock} (UPR={upr:.2f})')
  ax.hist(yReturns, bins="auto", density=True, label=f'x̄={smean:.2f}, s={ssdev:.2f}\nover [{smin:.2f}, {smax:.2f}]')
  ax.plot(xAxis, np.vectorize(lognormpdf)(xAxis, mu, sigma, tau, extremeIsMin), label=f'µ={mu:.2f}, σ={sigma:.2f},\nτ={tau:.2f}\nUP={up:.2f}, DD={dd:.2f}', color='tab:orange')
  ax.plot([smean, smean], [0, lognormpdf(smean, mu, sigma, tau, extremeIsMin)], label=None, color='tab:orange')
  ax.legend(fontsize='x-small')
  ax.get_yaxis().set_visible(False)
  ax.set_xlabel(name, fontsize='x-small')

  n += 1
  if (n < numStocks):
    col += 1
    if col >= cols:
      row += 1
      col = 0

if numStocks > 1:
  for c in range(col+1, cols):
    plt.delaxes(axs[row, c])
plt.savefig('UPR Chart.pdf')

portExcess = 0
for i in range(0, len(stocks)):
  if results[i][2] > 1:
    results[i][5] = round(results[i][2] / sum_upr * 100)
    if results[i][5] > maxPortPct:
      portExcess += (results[i][5] - maxPortPct)
      results[i][5] = maxPortPct

df = pd.DataFrame(results, columns = ['Name', 'DTR', 'UPR', 'UP', 'DD', 'UPR %'], index = stocks)
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', 1000)
formatters = {}
with open('UPR Table.txt', 'w') as file:
  df_string = df.to_markdown()
  if portExcess > 0:
    df_string += f'\n\nExcess Portfolio: %{portExcess}'
  file.write(df_string)
