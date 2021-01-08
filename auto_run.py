import schedule
import time
import datetime, pytz, holidays
import day_rules

# this bot is completely automatic running
# auto collecting data
# auto analyzing data
# trading using candlestick pattern
# set up function to run and indicate what is it doing



# schedule time for everything
# bot work monday to friday which mean 5 days a week
# starting with

# Monday


schedule.every().monday.at("18:00").do(day_rules.run_daily_data)

schedule.every().monday.at("9:00").do(day_rules.run_robinbot)

schedule.every().monday.at("9:30").do(day_rules.run_robinbot)

schedule.every().monday.at("10:00").do(day_rules.run_robinbot)

schedule.every().monday.at("10:30").do(day_rules.run_robinbot)

schedule.every().monday.at("11:00").do(day_rules.run_robinbot)

schedule.every().monday.at("11:30").do(day_rules.run_robinbot)

schedule.every().monday.at("12:00").do(day_rules.run_robinbot)

schedule.every().monday.at("12:30").do(day_rules.run_robinbot)

schedule.every().monday.at("13:00").do(day_rules.run_robinbot)

schedule.every().monday.at("13:30").do(day_rules.run_robinbot)

schedule.every().monday.at("14:00").do(day_rules.run_robinbot)

schedule.every().monday.at("14:30").do(day_rules.run_robinbot)

schedule.every().monday.at("15:00").do(day_rules.run_robinbot)

# Tuesday

schedule.every().tuesday.at("18:00").do(day_rules.run_daily_data)

schedule.every().tuesday.at("9:00").do(day_rules.run_robinbot)

schedule.every().tuesday.at("9:30").do(day_rules.run_robinbot)

schedule.every().tuesday.at("10:00").do(day_rules.run_robinbot)

schedule.every().tuesday.at("10:30").do(day_rules.run_robinbot)

schedule.every().tuesday.at("11:00").do(day_rules.run_robinbot)

schedule.every().tuesday.at("11:30").do(day_rules.run_robinbot)

schedule.every().tuesday.at("12:00").do(day_rules.run_robinbot)

schedule.every().tuesday.at("12:30").do(day_rules.run_robinbot)

schedule.every().tuesday.at("13:00").do(day_rules.run_robinbot)

schedule.every().tuesday.at("13:30").do(day_rules.run_robinbot)

schedule.every().tuesday.at("14:00").do(day_rules.run_robinbot)

schedule.every().tuesday.at("14:30").do(day_rules.run_robinbot)

schedule.every().tuesday.at("15:00").do(day_rules.run_robinbot)

# Wednesday

schedule.every().wednesday.at("18:00").do(day_rules.run_daily_data)

schedule.every().wednesday.at("9:00").do(day_rules.run_robinbot)

schedule.every().wednesday.at("9:30").do(day_rules.run_robinbot)

schedule.every().wednesday.at("10:00").do(day_rules.run_robinbot)

schedule.every().wednesday.at("10:30").do(day_rules.run_robinbot)

schedule.every().wednesday.at("11:00").do(day_rules.run_robinbot)

schedule.every().wednesday.at("11:30").do(day_rules.run_robinbot)

schedule.every().wednesday.at("12:00").do(day_rules.run_robinbot)

schedule.every().wednesday.at("12:30").do(day_rules.run_robinbot)

schedule.every().wednesday.at("13:00").do(day_rules.run_robinbot)

schedule.every().wednesday.at("13:30").do(day_rules.run_robinbot)

schedule.every().wednesday.at("14:00").do(day_rules.run_robinbot)

schedule.every().wednesday.at("14:30").do(day_rules.run_robinbot)

schedule.every().wednesday.at("15:00").do(day_rules.run_robinbot)

# Thursday

schedule.every().thursday.at("18:00").do(day_rules.run_daily_data)

schedule.every().thursday.at("9:00").do(day_rules.run_robinbot)

schedule.every().thursday.at("9:30").do(day_rules.run_robinbot)

schedule.every().thursday.at("10:00").do(day_rules.run_robinbot)

schedule.every().thursday.at("10:30").do(day_rules.run_robinbot)

schedule.every().thursday.at("11:00").do(day_rules.run_robinbot)

schedule.every().thursday.at("11:30").do(day_rules.run_robinbot)

schedule.every().thursday.at("12:00").do(day_rules.run_robinbot)

schedule.every().thursday.at("12:30").do(day_rules.run_robinbot)

schedule.every().thursday.at("13:00").do(day_rules.run_robinbot)

schedule.every().thursday.at("13:30").do(day_rules.run_robinbot)

schedule.every().thursday.at("14:00").do(day_rules.run_robinbot)

schedule.every().thursday.at("14:30").do(day_rules.run_robinbot)

schedule.every().thursday.at("15:00").do(day_rules.run_robinbot)

# friday

schedule.every().friday.at("18:00").do(day_rules.run_daily_data)

schedule.every().friday.at("9:00").do(day_rules.run_robinbot)

schedule.every().friday.at("9:30").do(day_rules.run_robinbot)

schedule.every().friday.at("10:00").do(day_rules.run_robinbot)

schedule.every().friday.at("10:30").do(day_rules.run_robinbot)

schedule.every().friday.at("11:00").do(day_rules.run_robinbot)

schedule.every().friday.at("11:30").do(day_rules.run_robinbot)

schedule.every().friday.at("12:00").do(day_rules.run_robinbot)

schedule.every().friday.at("12:30").do(day_rules.run_robinbot)

schedule.every().friday.at("13:00").do(day_rules.run_robinbot)

schedule.every().friday.at("13:30").do(day_rules.run_robinbot)

schedule.every().friday.at("14:00").do(day_rules.run_robinbot)

schedule.every().friday.at("14:30").do(day_rules.run_robinbot)

schedule.every().friday.at("15:00").do(day_rules.run_robinbot)

schedule.every().saturday.at("12:00").do(day_rules.run_ticker_data())
# running time
while True:
    schedule.run_pending()
    time.sleep(1)
