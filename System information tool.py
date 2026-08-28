import platform
import os

print("----- System Information -----")

print("Operating System:", platform.system())
print("OS Version:", platform.version())
print("Machine:", platform.machine())
print("Processor:", platform.processor())
print("Python Version:", platform.python_version())
print("CPU Cores:", os.cpu_count())
