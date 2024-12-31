import time
import threading
import random
from win10toast import ToastNotifier

def toaster_message():
    messages = [
        "Take a break",
        "It's time to chill",
        "Vreme je za pauzu!",
        "PAUZA!!!",
        "Ej bre, stani malo, gricka cipi-cips...",
        "Ajde i PC ti je umoran..."
    ]

    while True:
        toaster = ToastNotifier()
        random_item = random.choice(messages)
        toaster.show_toast("Reminder!", random_item, duration=5)
        time.sleep(30)

thread_toaster_message = threading.Thread(target=toaster_message)
thread_toaster_message.start()


temp_var=0
while temp_var < 20:
    temp_var =+1
    print("Prosao petlju")
    time.sleep(2)