import psutil

def get_system_resources():
  cpu_usage = psutil.cpu_percent(interval=1)

  memory = psutil.virtual_memory()
  memory_used = psutil.used / (1024**3)
  memory_total = memory.total / (1024**3)

  disk = psutil.disk_usage("/")
  disk_used = disk.used / (1024**3)
  disk_total = disk.total / (1024**3)

  return {
    "CPU": f"{cpu_usage}%",
    "Memory": f"{memory_used:.2f}/{memory_total:.2f}",
    "Disk": f"{disk_used:.2f}/{disk_total:.2f}",
  }

resources = get_system_resources()

for name, usage in resources.items():
  print(f"name: {name} usage: {usage}")
