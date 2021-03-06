import os
import yahoo_fin.stock_info as si
from yahoo_fin import options
import day_rules
print('Run 3 days collector!')

arr3 = os.listdir('Small_data')
if len(arr3) != 0:
    for i in range(len(arr3)):
        j = 'Small_data\\' + arr3[i]
        percent = i / len(arr3) * 100
        print('Cleaning old folder! -- ', percent, '%')
        os.remove(j)


print('Create ticker list!')
arr = os.listdir('Big_data')
arr.sort()
tt = 'Big_data\\'
arr2 = []
for each in range(len(arr)):
    ttt = tt + arr[each]
    b = os.path.getsize(ttt)
    if b > 1000:
        arr2 = arr2 + [arr[each]]


print('Create ticker name list')
data2 = day_rules.rename_generator(arr2)

for each in range(len(data2)):
    c = tt + data2[each] + '_stock.txt'
    big_file = open(c, 'r')
    lines = big_file.readlines()
    lines = lines[(len(lines)-3):(len(lines))]
    big_file.close()
    a = 'Small_data\\'
    b = data2[each] + '_stock.txt'
    x = a + b
    print('Creating file ', b, ' in ', a)
    company_file = open(x, 'w')
    content2 = []
    for i in range(3):
        content = lines[i]
        content = content[11:]
        content2 = content2 + [float(content.split()[5])]
        if '\n' in content:
            content = content.replace('\n', '')
        company_file.write(content)
        company_file.write('\n')
    company_file.close()
    if 0 in content2:
        os.remove(x)
    percentage = each / len(data2) * 100
    print('I did ', round(percentage, 3), ' % of the process!')


print('Finished 3 days collector!')
