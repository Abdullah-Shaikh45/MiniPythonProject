import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(title="Please Drink water Now!", message="A healthy adult generally needs around 3.7 liters (15.5 cups) of fluids per day for men and 2.7 liters (11.5 cups) for women. This can be met through various sources like water, other beverages, and even some water-rich foods. ", app_icon = "water-icon.ico", timeout = 5)
        time.sleep(60*60)
        
