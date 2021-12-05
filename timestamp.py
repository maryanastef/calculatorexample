import time
import datetime

date = datetime.datetime.now()
timestamp = datetime.datetime.timestamp(date) * 1000
print(timestamp)
