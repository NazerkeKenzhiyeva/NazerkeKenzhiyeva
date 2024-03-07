import datetime

NOW = datetime.datetime.now()
fiveDays = NOW - datetime.timedelta(days=5)
print(fiveDays.strftime("%Y-%m-%d"))

