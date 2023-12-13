import sys, time, os, psutil

from data_processor import DataProcessor

dp = DataProcessor()
for i in range(4):
    dp.add_file(f"tests/doc{i}")

# testing the validity edge cases
assert(dp.occur_dict["this"] == [[2, 1, 1, 1], [0, 1, 0], [0, 0, 1]])
assert(dp.occur_dict["the"] == [[], [], [0, 2, 0]])
assert(dp.occur_dict["test"] == [[1,0,1,0], [0,1,1]])
assert(dp.occur_dict["lorem"] == [[], [1, 0, 0], [], [2, 0, 1, 0, 1, 1, 0, 0]])

# testing the speed
file_count = 20
time_limit = 0.5
try:
    file_count = int(sys.argv[1])
    time_limit = float(sys.argv[2])
except (IndexError):
    pass

start_time = time.time()
init_ram = psutil.Process(os.getpid()).memory_info().rss
dp = DataProcessor()
max_ram = 0
for i in range(file_count):
    dp.add_file(f"data/document_{i}.txt")
    ram = psutil.Process(os.getpid()).memory_info().rss
    max_ram = max(ram, max_ram)
end_time = time.time()
exec_time = end_time-start_time
print(f"Adding {file_count} files took {exec_time} seconds")
print(f"Max RAM usage of DP was {(max_ram-init_ram)/1024**2} MiB (actual usage was {max_ram/1024**2} MiB)")
assert(exec_time < time_limit)

print("Tests are completed successfully!")
