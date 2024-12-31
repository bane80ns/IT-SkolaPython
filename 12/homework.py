import psutil

cpu_usage = psutil.cpu_percent(interval=5)
logical_cores = psutil.cpu_count()
phys_cores = psutil.cpu_count(logical=False)
current_process = psutil.Process()
num_threads = current_process.num_threads()


print(f"\n"
      f"Total CPU Usage: {cpu_usage}%\n"
      f"Number of Physical Cores: {phys_cores}\n"
      f"Number of Logical Cores: {logical_cores}\n"
      f"Number of Threads in Current Process: {num_threads}\n")
