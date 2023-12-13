import sys, time, os
import psutil

from data_processor import DataProcessor

dp = DataProcessor()
doc_size_test = 4
for i in range(doc_size_test):
    dp.add_file(f"tests/doc{i}")

# testing the validity edge cases
tests = [(dp.occur_dict["lorem"],{1:[1, 0, 0], 3:[2, 0, 1, 0, 1, 1, 0, 0]}),
         (dp.occur_dict["test"], {0:[1,0,1,0], 1:[0,1,1]}),
         (dp.occur_dict["the"], {2:[0,2,0]}),
         (dp.occur_dict["this"], {0:[2,1,1,1],1:[0,1,0],2:[0,0,1]}),
         ]

for actual,test in tests:
    # t sands for test, a stands for actual
    for adict, tdict in zip(actual.items(), test.items()):
        akey, aarray = adict
        tkey, tarray = tdict
        assert aarray.tolist() == tarray
        assert akey == tkey

# occurences calculation
assert(dp.document_occurences("lorem", 1) == 1)
assert(dp.document_occurences("lorem", 3) == 5)
assert(dp.occurences("lorem") == 6)

assert(dp.document_occurences("this", 3) == 0)
assert(dp.occurences("this") == 7)
assert(dp.document_occurences("this", 0) == 5)

# error handling
try:
    dp.occurences("madeupword")
    assert(False)
except(RuntimeError):
    pass

try:
    dp.document_occurences("test",doc_size_test)
    assert(False)
except(RuntimeError):
    pass

# testing the speed
file_count = 200
time_limit = 0.25
calculate_occurances = 0
try:
    file_count = int(sys.argv[1])
    calculate_occurances = int(sys.argv[2])
    time_limit = float(sys.argv[3])
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

if calculate_occurances:
    for word in dp.occur_dict:
        dp.occurences(word)

end_time = time.time()
exec_time = end_time-start_time
print(f"Adding {file_count} files took {exec_time} seconds", end=" ")
if calculate_occurances:
    print("(Occurances were calculated too)")
else:
    print()
print(f"Max RAM usage of DP was {(max_ram-init_ram)/1024**2} MiB (actual usage was {max_ram/1024**2} MiB)")
assert(exec_time < time_limit)

print("Tests are completed successfully!")
