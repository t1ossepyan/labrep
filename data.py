#1

import datetime

current_date = datetime.datetime.today()
new_date = current_date - datetime.timedelta(days=5)

print(new_date)

#2

from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#3

from datetime import datetime

current_time = datetime.now().replace(microsecond=0)

print("Current Time without Microseconds:", current_time)

#4

from datetime import datetime

date1 = datetime(2024, 2, 10, 12, 0, 0)  # Example date 1
date2 = datetime(2024, 2, 15, 14, 30, 0)  # Example date 2

difference = abs((date2 - date1).total_seconds())

print("Difference in Seconds:", difference)
