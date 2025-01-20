"""
f-string only works with Python 3 and above
"""
cpu_usage = 10
memory_used = 0.5
memory_total = 1

# f-string
print("CPU usage" + f"{cpu_usage}%") # output: CPU usage10%
print(f"{memory_used:.2f}/{memory_total:.2f}") # output: 0.50/1.00

# old passion
print("CPU usage {usage}%".format(usage=cpu_usage)) # output: CPU usage10%
print("CPU usage {0}% and memory used {1}".format(10, 0.5)) # output: CPU usage 10% and memory used 0.5
