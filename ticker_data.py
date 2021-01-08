import yahoo_fin.stock_info as si
import day_rules
import os

print('Starting create list')
data = open('tickers_name.txt', 'r')
number_of_ticker = len(data.readlines())
data.close()
print('Starting creating file')
arr3 = os.listdir('Big_data')
if len(arr3) != 0:
    for i in range(len(arr3)):
        j = 'Big_data\\' + arr3[i]
        percent = i / len(arr3) * 100
        print('Cleaning old folder! -- ', round(percent, 3), '%')
        os.remove(j)
print('Cleaning old folder! --  100 %')
print('Finish Cleaning Old Big_data!')

for each in range(number_of_ticker):
    big_file = open('tickers_name.txt', 'r')
    lines = big_file.readlines()
    each1 = lines[each]
    big_file.close()
    each1 = each1.replace('\n', '')

    a = 'Big_data\\'
    b = each1 + '_stock.txt'

    x = a + b
    print('Creating file', x)
    percentage = each / number_of_ticker * 100
    print('I did ', round(percentage, 3), ' % of the process!')
    if day_rules.is_valid_code(each1):

        company_file = open(x, 'w')

        data = si.get_data(each1)

        for i in range(1, len(data)):
            value_content = str(data.values[i])
            if '\n' in value_content:
                value_content = value_content.replace('\n', '')
            if '[' in value_content:
                value_content = value_content.replace('[', '')
            if ']' in value_content:
                value_content = value_content.replace('[', '')
            if ']' in value_content:
                value_content = value_content.replace('[', '')
            date_content = str(data.index[i])
            date_content = date_content[0:10]
            content = date_content + ' ' + value_content
            x = len(content) - 1
            content = content[0:x]
            company_file.write(content)
            company_file.write('\n')

        company_file.close()
    else:
        continue

print('Done Big_data')

