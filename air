import time
import datetime
import winsound

def set_alarm(alarm_time):
    """Set an alarm for a specific time."""
    print(f"Going to bed now. Alarm set for {alarm_time.strftime('%H:%M:%S')}.")
    while datetime.datetime.now() < alarm_time:
        time.sleep(1)
    print("Wake up! It's time to start your day!")
    for i in range(10):  # The alarm will beep 10 times
        winsound.Beep(2500, 1000)  # Beep at 2500 Hz for 1000 milliseconds

if __name__ == "__main__":
    # Set the alarm for the next minute
    current_time = datetime.datetime.now()
    alarm_time = (current_time + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
    set_alarm(alarm_time)