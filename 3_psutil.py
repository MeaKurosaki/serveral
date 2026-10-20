import psutil

logical_cores = psutil.cpu_count(logical=True)
physical_cores = psutil.cpu_count(logical=False)

print(f"Logical cores : {logical_cores}")
print(f"Physical cores : {physical_cores}")

per_cpu_percent = psutil.cpu_percent(interval=1,percpu=True)
for i,per in enumerate(per_cpu_percent):
    print(f"CPU {i} : {per}%")