import robin_stocks as r
from robin_stocks import *
import pyotp
import os
import day_rules

# please enter your robinhood acount and password below
# DO NOT RUN THIS FILE, JUST ENTER YOUR ACCOUNT AND PASSWORD, THEN SAVE IT, AND CLOSE IT
# login to robinhood account
# enter your robinhood account between the quotes
your_account = 'enter your account here'
# enter your robinhood password between the quotes
# after enter your password, now you have done everything you need, close this file and run auto.py
your_password = 'enter your password here'
login = r.login(your_account, your_password)
totp = pyotp.TOTP("My2factorAppHere").now()
print("Current OTP:", totp)
my_stocks = r.build_holdings()
my_key = []
my_set_quantity = []
my_quantity = []
my_percent_change = []
# print out all of our investment ticker and value
for key, value in my_stocks.items():
    print(key, value)
    my_key = my_key + [key]
    my_set_quantity = my_set_quantity + [value]

for each in range(len(my_key)):
    my_quantity = my_quantity + [int(float(my_set_quantity[each]['quantity']))]
    my_percent_change = my_percent_change + [float(my_set_quantity[each]['percent_change'])]

# print account balance and total investment
cash_in_account = r.profiles.load_account_profile('portfolio_cash')
print('Cash in account = ', cash_in_account)
print('Total Investment = ', r.profiles.load_portfolio_profile('market_value'))
# set quantity
quantity = 1
# read buy and sell ticker from file
buy_text = 'Buy_signal'
sell_text = 'Sell_signal'
buy_folder = os.listdir(buy_text)
buy_directory = str(max(day_rules.buy_rename_to_number(buy_folder)))
buy_directory = buy_text + '\\' + buy_directory + '.txt'
sell_folder = os.listdir(sell_text)
sell_directory = str(max(day_rules.sell_rename_to_number(sell_folder)))
sell_directory = sell_text + '\\' + sell_directory + 'txt'

# read buy signal file created from last night
buy_file = open(buy_directory, 'r')
lines = buy_file.readlines()
buy_list = []
for each in range(len(lines) - 1):
    buy_list = buy_list + [lines[each]]
buy_file.close()

# read sell signal file created from last night
sell_file = open(sell_directory, 'r')
lines = sell_file.readlines()
sell_list = []
for each in range(len(lines) - 1):
    sell_list = sell_list + [lines[each]]
sell_file.close()

# sell all of stock need to sell
for each in range(len(sell_list)):
    if sell_list[each] in my_key:
        x = day_rules.arrayfinder(my_key, sell_list[each])
        if my_percent_change[x] > 0:
            r.orders.order_sell_market(sell_list[each], my_quantity[x])
            print('I sold ticker: ', sell_list[each], 'at price: ',
                  r.get_latest_price(sell_list[each]), 'and percentage change at: ', my_percent_change[x])


# buy every stock can be bought if we have money
buy_queue = []
cash_in_account = r.profiles.load_account_profile('portfolio_cash')
print('You have ', cash_in_account, ' in account balance after selling')
for each in range(len(buy_list)):
    latest_price = r.get_latest_price(buy_list[each])

# changing quantity depend on the latest price of stock
    if 700 < latest_price <= 900:
        quantity = 2
    elif 500 < latest_price <= 700:
        quantity = 3
    elif 300 < latest_price <= 500:
        quantity = 4
    elif 200 < latest_price <= 300:
        quantity = 5
    elif 150 < latest_price <= 200:
        quantity = 10
    elif 100 < latest_price <= 150:
        quantity = 15
    elif 50 < latest_price <= 100:
        quantity = 20
    elif 40 < latest_price <= 50:
        quantity = 30
    elif 30 < latest_price <= 40:
        quantity = 40
    elif 25 < latest_price <= 30:
        quantity = 50
    elif 20 < latest_price <= 25:
        quantity = 60
    elif 15 < latest_price <= 20:
        quantity = 70
    elif 10 < latest_price <= 15:
        quantity = 90
    elif 5 < latest_price <= 10:
        quantity = 180
    elif 4 < latest_price <= 5:
        quantity = 300
    elif 3 < latest_price <= 4:
        quantity = 400
    elif 2 < latest_price <= 3:
        quantity = 500
    elif 1.5 < latest_price <= 2:
        quantity = 750
    elif 1 < latest_price <= 1.5:
        quantity = 1000
    elif 0.75 < latest_price <= 1:
        quantity = 1400
    elif 0.5 < latest_price <= 0.75:
        quantity = 2300
    elif 0.25 < latest_price <= 0.5:
        quantity = 3500
    elif 0.2 < latest_price <= 0.25:
        quantity = 6000
    elif latest_price <= 0.2:
        quantity = 10000
# Buying stock if we have money
    if latest_price * quantity < cash_in_account and buy_list[each] not in my_key:
        r.order_buy_market(buy_list[each], quantity)
        cash_in_account = cash_in_account - (latest_price * quantity)
        print('I bought ', buy_list[each], 'for you at $', latest_price)

# Summary account
print('Account summary')
for key, value in my_stocks.items():
    print(key, value)
cash_in_account = r.profiles.load_account_profile('portfolio_cash')
print('Cash in account = ', cash_in_account)
print('Total Investment = ', r.profiles.load_portfolio_profile('market_value'))
