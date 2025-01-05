from playsound import playsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_lef = time_left %60

        print(f"{minutes_left:02d}:{seconds_lef:02d}")

    playsound("alarm.mp3")

minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)