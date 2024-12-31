import psutil
import time

processes = list(psutil.process_iter(["name", "memory_percent", "cpu_percent"]))

"""
for proc in processes:
    print(proc)
"""
for proc in processes:
    proc.cpu_percent(interval=None)

time.sleep(1)

print(f"{"      NAME":<28}{"        MEMORY":<20}{"    CPU":<5}")

for proc in processes:
    print(f"Name: {proc.name():<27}   Memory: {proc.memory_percent():<5.2f}   CPU: {proc.cpu_percent():<28}")
