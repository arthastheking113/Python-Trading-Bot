import time
import os
import yahoo_fin.stock_info as si
import datetime, pytz, holidays


def error(high_price):
    return high_price * 0.05


# bullish candlestick pattern
def hammer(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if close_price1 <= open_price1 and high_price1 <= (close_price1 + error(high_price1)) \
            and open_price1 > (((high_price1 - low_price1) / 2) + low_price1) \
            and close_price2 > open_price2 and close_price3 > open_price3:
        return 1
    else:
        return 0


def inverse_hammer(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if open_price1 < close_price1 < (((high_price1 - low_price1) / 2) + low_price1) \
            and low_price1 <= (open_price1 - error(high_price1)) \
            and close_price2 > open_price2 and close_price3 > open_price3:
        return 1
    else:
        return 0


def bullish_engulfing(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]

    # compare day2 and day3
    if close_price2 < open_price2 and close_price3 - open_price3 > open_price2 - close_price2 \
            and open_price3 < open_price2:
        return 1
    # compare day1 and day2
    elif close_price1 < open_price1 and close_price2 - open_price2 > open_price1 - close_price1 \
            and open_price2 < open_price1:
        return 1
    else:
        return 0


def piercing_line(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]

    # compare day1 and day2
    if close_price1 < open_price1 and (high_price1 - low_price1) * 0.75 > open_price1 - close_price1 \
            and close_price2 - open_price2 > 0 \
            and (((open_price1 - close_price1) / 2) + close_price1) < close_price2:
        return 1
    # compare day2 and day3
    elif close_price2 < open_price2 and (high_price2 - low_price2) * 0.75 > open_price2 - close_price2 \
            and close_price3 - open_price3 > 0 \
            and (((open_price2 - close_price2) / 2) + close_price2) < close_price3:
        return 1
    else:
        return 0


def morning_star(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if close_price1 < open_price1 and (open_price1 - close_price1) <= ((high_price1 - low_price1) * 0.95) \
            and (high_price2 - low_price2) * 0.3 >= abs(open_price2 - close_price2) \
            and close_price3 > open_price3 and (close_price3 - open_price3) <= ((high_price3 - low_price3) * 0.95):
        return 1
    else:
        return 0


def three_white_soldiers(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if close_price1 > open_price1 and close_price2 > open_price2 and close_price3 > open_price3:
        return 1
    else:
        return 0


def three_line_strike_bullish(day1, day2, day3, day4):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    # day4
    open_price4 = day4[0]
    high_price4 = day4[1]
    low_price4 = day4[2]
    close_price4 = day4[3]
    if open_price1 > close_price1 and open_price2 > close_price2 \
            and open_price3 > close_price3 and close_price4 > open_price4 \
            and close_price4 - open_price4 <= ((high_price4 - low_price4) * 0.95) \
            and open_price4 < close_price3 and close_price4 > open_price1:
        return 1
    else:
        return 0


# bearish candlestick pattern
def hanging_man(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if close_price1 <= open_price1 and high_price1 <= (close_price1 + error(high_price1)) \
            and open_price1 > (((high_price1 - low_price1) / 2) + low_price1) \
            and close_price2 < open_price2 and close_price3 < open_price3:
        return 1
    else:
        return 0


def shooting_star(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if open_price1 < close_price1 < (((high_price1 - low_price1) / 2) + low_price1) \
            and low_price1 <= (open_price1 - error(high_price1)) \
            and close_price2 < open_price2 and close_price3 < open_price3:
        return 1
    else:
        return 0


def bearish_engulfing(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]

    # compare day2 and day3
    if close_price2 > open_price2 and open_price3 - close_price3 > close_price2 - open_price2 \
            and open_price3 > open_price2:
        return 1
    # compare day1 and day2
    elif close_price1 > open_price1 and open_price2 - close_price2 > close_price1 - open_price1 \
            and open_price2 > open_price1:
        return 1
    else:
        return 0


def evening_star(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if close_price1 > open_price1 and (close_price1 - open_price1) <= ((high_price1 - low_price1) * 0.95) \
            and (high_price2 - low_price2) * 0.3 >= abs(open_price2 - close_price2) \
            and close_price3 < open_price3 and (open_price3 - close_price3) <= ((high_price3 - low_price3) * 0.95):
        return 1
    else:
        return 0


def three_black_crows(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if close_price1 < open_price1 and close_price2 < open_price2 and close_price3 < open_price3:
        return 1
    else:
        return 0


def dark_cloud_cover(day1, day2, day3):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    if open_price1 < close_price1 < open_price2 \
            and ((high_price1 - low_price1) * 0.9) >= (close_price1 - open_price1) \
            and open_price2 > close_price2 > open_price1 and close_price2 < close_price1:
        return 1
    else:
        return 0


def three_line_strike_bearish(day1, day2, day3, day4):
    # day1
    open_price1 = day1[0]
    high_price1 = day1[1]
    low_price1 = day1[2]
    close_price1 = day1[3]
    # day2
    open_price2 = day2[0]
    high_price2 = day2[1]
    low_price2 = day2[2]
    close_price2 = day2[3]
    # day3
    open_price3 = day3[0]
    high_price3 = day3[1]
    low_price3 = day3[2]
    close_price3 = day3[3]
    # day4
    open_price4 = day4[0]
    high_price4 = day4[1]
    low_price4 = day4[2]
    close_price4 = day4[3]
    if open_price1 < close_price1 and open_price2 < close_price2 \
            and open_price3 < close_price3 and close_price4 < open_price4 \
            and open_price4 - close_price4 <= ((high_price4 - low_price4) * 0.95) \
            and open_price4 > close_price3 and close_price4 < open_price1:
        return 1
    else:
        return 0


# function rules
def is_valid_code(line):
    try:
        assert si.get_data(line)
    except AssertionError:
        return False
    except ValueError:
        return True
    except KeyError:
        return False
    else:
        return True


def get_daily_data():
    arr = os.listdir('Big_data')
    arr.sort()
    arr = rename_generator(arr)
    number_of_ticker = len(arr)
    for each in range(number_of_ticker):
        lines = arr[each]
        a = 'Big_data\\'
        b = lines + '_stock.txt'  # each is ticker name
        x = a + b
        print('Adding data to file', x)
        percentage = each / number_of_ticker * 100
        print('I did ', round(percentage, 2), '% of the process!')
        if is_valid_code(lines):
            old_content = open(x, 'r')
            line = old_content.readlines()
            if not line:
                old_content.close()
            else:
                if line == 1:
                    last_data = old_content.readlines()[0]
                    old_content.close()
                    if '\n' in last_data:
                        last_data = last_data.replace('\n', '')
                    company_file = open(x, 'a')
                    data = si.get_data(each)
                    value_content = str(data.values[(len(data) - 1)])
                    if '\n' in value_content:
                        value_content = value_content.replace('\n', '')
                    if '[' in value_content:
                        value_content = value_content.replace('[', '')
                    if ']' in value_content:
                        value_content = value_content.replace('[', '')
                    if ']' in value_content:
                        value_content = value_content.replace('[', '')
                    date_content = str(data.index[(len(data) - 1)])
                    date_content = date_content[0:10]
                    content = date_content + ' ' + value_content
                    x = len(content) - 1
                    content = content[0:x]
                    if content != last_data:
                        company_file.write(content)
                        company_file.write('\n')
                    company_file.close()
                else:
                    last_data = line[-1]
                    old_content.close()
                    if '\n' in last_data:
                        last_data = last_data.replace('\n', '')
                    company_file = open(x, 'a')
                    data = si.get_data(lines)
                    value_content = str(data.values[(len(data) - 1)])
                    if '\n' in value_content:
                        value_content = value_content.replace('\n', '')
                    if '[' in value_content:
                        value_content = value_content.replace('[', '')
                    if ']' in value_content:
                        value_content = value_content.replace('[', '')
                    if ']' in value_content:
                        value_content = value_content.replace('[', '')
                    date_content = str(data.index[(len(data) - 1)])
                    date_content = date_content[0:10]
                    content = date_content + ' ' + value_content
                    x = len(content) - 1
                    content = content[0:x]
                    if content != last_data:
                        company_file.write(content)
                        company_file.write('\n')
                    company_file.close()


def rename_generator(list):
    rename = []
    for each in range(len(list)):
        name = list[each]
        name = name.replace('_stock.txt', '')
        rename = rename + [name]
    return rename


def rename(name):
    name = name.replace('_stock.txt', '')
    return name


def arrayfinder(list, x):
    if list[0] == x:
        return 0
    else:
        return 1 + arrayfinder(list[1:], x)


def afterHours(now=None):
    tz = pytz.timezone('US/Eastern')
    us_holidays = holidays.US()
    if not now:
        now = datetime.datetime.now(tz)
    openTime = datetime.time(hour=9, minute=30, second=0)
    closeTime = datetime.time(hour=16, minute=0, second=0)
    # If a holiday
    if now.strftime('%Y-%m-%d') in us_holidays:
        return True
    # If before 0930 or after 1600
    if (now.time() < openTime) or (now.time() > closeTime):
        return True
    # If it's a weekend
    if now.date().weekday() > 4:
        return True
    return False


def RSI(name_of_file):
    a = 'Medium_data\\'
    b = a + name_of_file
    file = open(b, 'r')
    data_line = []
    for each in range(15):
        rsi_data = file.readline()
        data_line = data_line + [float(rsi_data.split()[3])]
    file.close()
    rsi_value = RSI_indicator(data_line)
    return rsi_value


def RSI_indicator(list_data):
    up_move = []
    down_move = []
    if 16 < len(list_data) < 0:
        print('You need a list of 15 days to use RSI')
    else:
        for each in range(1,15):
            if list_data[each] > list_data[0]:
                value = list_data[each] - list_data[0]
                up_move = up_move + [value]
            elif list_data[each] < list_data[0]:
                value = list_data[each] - list_data[0]
                down_move = down_move + [abs(value)]
    average_up = sum(up_move)/14
    average_down = sum(down_move)/14
    if average_down == 0:
        value_data = 100
    else:
        rs = average_up/average_down
        value_data = 100 - (100/(rs + 1))
    return value_data


def run_ticker_name():
    print("I'm working: Generate all ticker name")
    print('It is 17:30')
    exec(open("tickers_name.py").read())


def run_ticker_data():
    print("I'm working: Collecting Big_data of all ticker")
    print('It is 18:00')
    exec(open("ticker_data.py").read())


def run_3day_collector():
    print("I'm working: Collecting Small_data of all ticker  ")
    print('It is 23:59')
    exec(open("3day_collector.py").read())


def run_3day_analizyer():
    print("I'm working: Analyzing Small_data of all ticker  ")
    print('It is 04:00')
    exec(open("3day_analizyer.py").read())


def run_robinbot():
    if not afterHours():
        print("I'm working: Running RobinBot to trade  ")
        print('Working Time')
        exec(open("robinbot.py").read())
    else:
        print("Don't wake me up!")
        print('Today is holiday, I need go to sleep!')


def run_daily_data():
    print('I am working now, updating big_data')
    exec(open("daily_data.py").read())


def run_RSI_data_collector():
    print('I am working now, Generate Medium_data')
    exec(open("RSI_data_collector.py").read())


def golden_cross(list49, list50, list199, list200):
    average49 = sum(list49) / 50
    average50 = sum(list50) / 50
    average199 = sum(list199) / 50
    average200 = sum(list200) / 200
    if average200 - error(average200) < average50 < average200 + error(average200) or \
            average50 - error(average50) < average200 < average50 + error(average50):
        if average49 < average50 and average199 > average200:
            return True
        else:
            return False
    else:
        return False


def death_cross(list49, list50, list199, list200):
    average49 = sum(list49) / 50
    average50 = sum(list50) / 50
    average199 = sum(list199) / 200
    average200 = sum(list200) / 200
    if average200 - error(average200) < average50 < average200 + error(average200) or \
            average50 - error(average50) < average200 < average50 + error(average50):
        if average49 > average50 and average199 < average200:
            return True
        else:
            return False
    else:
        return False


def buy_rename_to_number(list):
    list2 = []
    for each in range(len(list)):
        a = list[each]
        a = a.replace('.txt', '')
        a = int(a[10:])
        list2 = list2 + [a]
    list2.sort()
    return list2


def sell_rename_to_number(list):
    list2 = []
    for each in range(len(list)):
        a = list[each]
        a = a.replace('.txt', '')
        a = int(a[11:])
        list2 = list2 + [a]
    list2.sort()
    return list2


def golden_rename_to_number(list):
    list2 = []
    for each in range(len(list)):
        a = list[each]
        a = a.replace('.txt', '')
        a = int(a[12:])
        list2 = list2 + [a]
    list2.sort()
    return list2


def death_rename_to_number(list):
    list2 = []
    for each in range(len(list)):
        a = list[each]
        a = a.replace('.txt', '')
        a = int(a[11:])
        list2 = list2 + [a]
    list2.sort()
    return list2
