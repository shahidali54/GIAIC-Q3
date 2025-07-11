import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Time's up!")

t = input("Enter The Time In Seconds: ")

countdown(int(t)) 
# This code implements a simple countdown timer that takes user input in seconds and counts down to zero.