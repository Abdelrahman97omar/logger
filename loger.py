#!/usr/bin/env python3
from datetime import datetime
import pytz
import time as t


tz = pytz.timezone('Africa/Cairo')
# | Country      | pytz Timezone  |
# | ------------ | -------------- |
# | Egypt        | `Africa/Cairo` |
# | Saudi Arabia | `Asia/Riyadh`  |
# | UAE          | `Asia/Dubai`   |
file_name='logs.txt'

def get_time():
    now = datetime.now(tz)
    year = now.year
    month = now.month
    day = now.day
    current_time = now.strftime("%H:%M")
    return year, month, day, current_time

def main():

    year, month, day, current_time = get_time()

    with open(file_name, "a", encoding="utf-8") as f:
        f.write(f"This Pc started at: {current_time} {day}/{month}/{year}\n")
        f.write(f"Last seen at: {current_time} {day}/{month}/{year}\n")
        t.sleep(1)

    while True:
        year, month, day, current_time = get_time()
        with open(file_name, "r+", encoding="utf-8") as f:
            lines = f.readlines()
            lines[-1]=(f"Last seen at: {current_time} {day}/{month}/{year}\n")
            f.seek(0)
            f.writelines(lines)
            f.truncate()
        t.sleep(300)

if __name__=="__main__":
    main()
