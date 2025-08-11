import time
from TheList import unsorted_list

start_time = time.time()


sort1 = sorted(unsorted_list)
print(sort1[:10])
end_time = time.time()
# What is the difference between .sort and (sorted ?)
print(f"Execution time for native sorted : {end_time - start_time:.6f} seconds")
start_time2 = time.time()


unsorted_list.sort()
print(unsorted_list[:10])
end_time2 = time.time()
# What is the difference between .sort and (sorted ?)
print(f"Execution time for native sort : {end_time2 - start_time2:.6f} seconds")

start_time1 = time.time()

#Your Method

end_time1 = time.time()

print(f"Execution time for my first try to sort : {end_time1 - start_time1:.6f} seconds")
