import datetime as dt
import matplotlib.pyplot as plt
import os

from matplotlib import style
style.use('ggplot')

#import pandas as pd
#import pandas_datareader.data as web
from pandas_datareader import data as pdr


import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2017, 12, 5)

# download dataframe
ticker = 'ARRY'
def downloadHisData(ticker):
    data = pdr.get_data_yahoo(ticker, start="2000-01-01", end="2017-12-01")

    # download Panel
    #data = pdr.get_data_yahoo(["SPY", "TLSA"], start="2017-01-01", end="2017-04-30")

    # path = r'C:\java\pythonProjects\stockdemo\data'  # Saving path
    # file_name = r'\ticker_ADMP.csv'  # file name
    # dest_dir = os.path.join(path, file_name)  # located file

    data.to_csv('data/IBB/'+ticker+'.csv')