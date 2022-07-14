import time
time_1 = time.time()

time.sleep(5)

time_2 = time.time()
time_interval = time_2 - time_1
ntime_interval = format(time_interval, ".2f")
print('d')