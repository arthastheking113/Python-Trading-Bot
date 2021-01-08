import day_rules
print('Running daily update!')
print('Starting update data')
day_rules.get_daily_data()
print('Finished update daily data!')

exec(open("3day_collector.py").read())

exec(open("RSI_data_collector.py").read())

exec(open("moving_average.py").read())

exec(open("3day_analizyer.py").read())