import datetime as dt
import matplotlib.pyplot as plt

from matplotlib import style
style.use('ggplot')

#import pandas as pd
#import pandas_datareader.data as web
from pandas_datareader import data as pdr


import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12,30)
#df = web.DataReader('TLSA', 'yahoo', start, end)
# download dataframe
data = pdr.get_data_yahoo("AMZN", start="2017-01-01", end="2017-11-30")

# download Panel
#data = pdr.get_data_yahoo(["SPY", "TLSA"], start="2017-01-01", end="2017-04-30")
print(data.head())
print(data.tail(6))
data.to_csv('data/AMZN')