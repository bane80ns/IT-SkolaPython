import subprocess
import webbrowser
from win10toast import ToastNotifier
import time
import random

toaster = ToastNotifier()
toaster.show_toast("Reminder!", "Take a break!", duration=5)


messages = [
    "Take a break",
    "It's time to chill",
    "Vreme je za pauzu",
    "PAVZA"
]

# Open Notepad
# subprocess.Popen(["notepad.exe"])

# Open Pycharm
# subprocess.Popen(["C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\bin\pycharm64.exe"])

# webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://google.com")

while True:
    random_item = random.choice(messages)
    toaster.show_toast("Reminder!", random_item, duration=3)
    time.sleep(5)