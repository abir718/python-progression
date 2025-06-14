import time
import datetime

alarm_time = input("Set alarm (HH:MM in 24hr format): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("⏰ Wake up! Time's up!")
        break
    time.sleep(30)
