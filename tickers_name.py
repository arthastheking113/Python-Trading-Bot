import yahoo_fin.stock_info as si
from yahoo_fin import options
import os

dow = si.tickers_dow()
nasdaq = si.tickers_nasdaq()
sp500 = si.tickers_sp500()

tickers = dow + nasdaq + sp500
tickers.sort()
number_of_ticker = len(tickers)

os.makedirs('Big_data')
os.makedirs('Small_data')
os.makedirs('Medium_data')
os.makedirs('Buy_signal')
os.makedirs('Sell_signal')
os.makedirs('Moving_average')
os.makedirs('Moving_average\\50_days')
os.makedirs('Moving_average\\200_days')
os.makedirs('Moving_average\\cross')
os.makedirs('Moving_average\\cross\\death')
os.makedirs('Moving_average\\cross\\golden')

file = open('tickers_name.txt', 'w')
for x in range(number_of_ticker):
    file.write(tickers[x])
    file.write('\n')
    print('Adding ticker name', tickers[x], 'to folder')
file.close()


print('Done')