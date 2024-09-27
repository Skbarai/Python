import time 
from plyer import notification
set_time=float(input("Enter the hour after which you want to drink water: "))
while True:
    time.sleep(3600*set_time)
    notification.notify(title="Drink water", message="Hey santosh its time to drink water", timeout =2)