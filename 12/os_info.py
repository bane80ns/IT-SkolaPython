import psutil



memory_info = psutil.virtual_memory()
print(memory_info[0])

memory_info_inGB = (memory_info[0]) / (1024**3)
print(memory_info_inGB.__round__(2))

