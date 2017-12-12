import pandas as pd
import downloadTickerHisData as dhis

#read all IBB tickers from csv
df = pd.read_csv('data/IBB_holdings_sorted.csv',low_memory=False, delimiter='\t', header=0, encoding='ascii')
print(df.head(3))
#df=df.head(3)
#ticker_list=df["Ticker"].values
ticker_list=df["Ticker"].tolist()
print(ticker_list)

for t in ticker_list:
    dhis.downloadHisData(t)