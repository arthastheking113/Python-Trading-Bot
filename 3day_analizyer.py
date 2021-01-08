import os
import yahoo_fin.stock_info as si
import day_rules

print('Running 3 days analizyer')
buy_text = 'Buy_signal'
sell_text = 'Sell_signal'
buy_folder = os.listdir(buy_text)
sell_folder = os.listdir(sell_text)
golden_cross_folder = os.listdir('Moving_average\\cross\\golden')
death_cross_folder = os.listdir('Moving_average\\cross\\death')


a = 'Small_data'
arr = os.listdir(a)
arr.sort()
data = day_rules.rename_generator(arr)
# create buy folder
if 'buy_signal1.txt' not in buy_folder:
    a1 = 'Buy_signal\\buy_signal1.txt'
    signal_file = open(a1, 'w')
    signal_file.close()
    print('Creating file ', a1)
else:
    a1 = max(day_rules.buy_rename_to_number(buy_folder)) + 1
    a1 = 'Buy_signal\\buy_signal' + str(a1) + '.txt'
    signal_file = open(a1, 'w')
    signal_file.close()
    print('Creating file ', a1)
# create sell folder
if 'sell_signal1.txt' not in sell_folder:
    a2 = 'Sell_signal\\sell_signal1.txt'
    signal_file = open(a2, 'w')
    signal_file.close()
    print('Creating file ', a2)
else:
    a2 = max(day_rules.sell_rename_to_number(sell_folder)) + 1
    a2 = 'Sell_signal\\sell_signal' + str(a2) + '.txt'
    signal_file = open(a2, 'w')
    signal_file.close()
    print('Creating file ', a2)
# create golden cross folder
if 'golden_cross1.txt' not in golden_cross_folder:
    a3 = 'Moving_average\\cross\\golden\\golden_cross1.txt'
    signal_file = open(a3, 'w')
    signal_file.close()
    print('Creating file ', a3)
else:
    a3 = max(day_rules.golden_rename_to_number(golden_cross_folder)) + 1
    a3 = 'Moving_average\\cross\\golden\\golden_cross' + str(a3) + '.txt'
    signal_file = open(a3, 'w')
    signal_file.close()
    print('Creating file ', a3)
# create deadth cross folder
if 'death_cross1.txt' not in death_cross_folder:
    a4 = 'Moving_average\\cross\\death\\death_cross1.txt'
    signal_file = open(a4, 'w')
    signal_file.close()
    print('Creating file ', a4)
else:
    a4 = max(day_rules.death_rename_to_number(death_cross_folder)) + 1
    a4 = 'Moving_average\\cross\\death\\death_cross' + str(a4) + '.txt'
    signal_file = open(a4, 'w')
    signal_file.close()
    print('Creating file ', a4)

for each in range(len(arr)):
    b = 'Small_data\\'
    x = b + arr[each]
    file = open(x, 'r')
    lines = file.readlines()
    # transfrom str to num
    # day1
    day1 = lines[0]
    day1 = day1.split()
    for i in range(4):
        day1[i] = float(day1[i])
    # day2
    day2 = lines[1]
    day2 = day2.split()
    for i in range(4):
        day2[i] = float(day2[i])
    # day3
    day3 = lines[2]
    day3 = day3.split()
    for i in range(4):
        day3[i] = float(day3[i])
    # check buying signal
    buy = day_rules.hammer(day1, day2, day3) + day_rules.inverse_hammer(day1, day2, day3) \
          + day_rules.bullish_engulfing(day1, day2, day3) + day_rules.piercing_line(day1, day2, day3) \
          + day_rules.morning_star(day1, day2, day3) + day_rules.three_white_soldiers(day1, day2, day3)
    # check selling signal
    sell = day_rules.hanging_man(day1, day2, day3) + day_rules.shooting_star(day1, day2, day3) \
           + day_rules.bearish_engulfing(day1, day2, day3) + day_rules.evening_star(day1, day2, day3) \
           + day_rules.three_black_crows(day1, day2, day3) + day_rules.dark_cloud_cover(day1, day2, day3)
    arr3 = os.listdir('Medium_data')
    arr4 = os.listdir('Moving_average\\50_days\\')
    arr5 = os.listdir('Moving_average\\200_days\\')
    ass = arr[each]
    if buy > sell and ass in arr3 and ass in arr4 and ass in arr5:

        RSI = day_rules.RSI(arr[each])

        file_name1 = 'Moving_average\\50_days\\' + ass
        data49 = []
        file49 = open(file_name1, 'r')
        lines49 = file49.readlines()
        file49.close()

        for i in range(50):
            number49 = lines49[i]
            number49 = float(number49.split()[3])
            data49 = data49 + [number49]
        data50 = lines49[50]
        data50 = data49[1:] + [float(data50.split()[3])]

        file_name2 = 'Moving_average\\200_days\\' + ass
        data199 = []
        file199 = open(file_name2, 'r')
        lines199 = file199.readlines()
        file199.close()
        for i in range(200):
            number199 = lines199[i]
            number199 = float(number199.split()[3])
            data199 = data199 + [number199]
        data200 = lines199[200]
        data200 = data199[1:] + [float(data200.split()[3])]
        if RSI < 30 and day_rules.golden_cross(data49, data50, data199, data200):
            golden_folder = open(a4, 'a')
            golden_folder.write(day_rules.rename(ass))
            golden_folder.write('\n')
            golden_folder.close()

            signal_file = open(a1, 'a')
            signal_file.write(day_rules.rename(arr[each]))
            signal_file.write('\n')
            print('added ticker ', day_rules.rename(arr[each]), 'to buying signal with buying value = ', buy, 'to file', a1)
            print(day_rules.rename(arr[each]), 'has RSI = ', RSI)
            signal_file.close()
    elif sell > buy and ass in arr3 and ass in arr4 and ass in arr5:

        RSI = day_rules.RSI(arr[each])

        file_name1 = 'Moving_average\\50_days\\' + ass
        data49 = []
        file49 = open(file_name1, 'r')
        lines49 = file49.readlines()
        file49.close()

        for i in range(50):
            number49 = lines49[i]
            number49 = float(number49.split()[3])
            data49 = data49 + [number49]
        data50 = lines49[50]
        data50 = data49 + [float(data50.split()[3])]

        file_name2 = 'Moving_average\\200_days\\' + ass
        data199 = []
        file199 = open(file_name2, 'r')
        lines199 = file199.readlines()
        file199.close()
        for i in range(200):
            number199 = lines199[i]
            number199 = float(number199.split()[3])
            data199 = data199 + [number199]
        data200 = lines199[200]
        data200 = data199 + [float(data200.split()[3])]
        if RSI > 70 and day_rules.golden_cross(data49, data50, data199, data200):
            golden_folder = open(a3, 'a')
            golden_folder.write(day_rules.rename(ass))
            golden_folder.write('\n')
            golden_folder.close()

            signal_file = open(a2, 'a')
            signal_file.write(day_rules.rename(arr[each]))
            signal_file.write('\n')
            print('added ticker ', day_rules.rename(arr[each]), 'to selling signal with selling value = ', sell,
                  'to file', a2)
            print(day_rules.rename(arr[each]), 'has RSI = ', RSI)
            signal_file.close()
    percentage = each / len(arr) * 100
    print('I did', round(percentage, 2), '% of the process!')

print('I did 100 % of the process!')
print('Finished generate buy and sell list!')
