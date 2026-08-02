from datetime import datetime
import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time, end="\r")

    if current_time == alarm_time:
        print("\nAlarm! Wake up!")
        for i in range(5):
            print("Beep!")
            time.sleep(1)
        break

    time.sleep(1)
