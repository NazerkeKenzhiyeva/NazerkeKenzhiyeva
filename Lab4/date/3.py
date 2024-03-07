import datetime

NOW = datetime.datetime.now()

#1 way
woMicro = NOW.replace(microsecond=0)
print(woMicro)

#2 way
print(NOW.strftime("%Y-%m-%d" " %H:%M:%S"))