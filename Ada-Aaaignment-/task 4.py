# Solving Recurrences Through Code

import time


# 1️ T(n) = T(n/2) + n
# Expected Complexity: O(n)


calls_1 = 0

def recurrence_1(n):
    global calls_1
    calls_1 += 1
    
    if n <= 1:
        return 1
    
    # Work done at current level = n
    return recurrence_1(n // 2) + n



# 2️ T(n) = 2T(n/2) + n
# Expected Complexity: O(n log n)


calls_2 = 0

def recurrence_2(n):
    global calls_2
    calls_2 += 1
    
    if n <= 1:
        return 1
    
    # Two recursive calls
    return recurrence_2(n // 2) + recurrence_2(n // 2) + n



# Experiment


input_sizes = [8, 16, 32, 64, 128]

print("n | Rec1_Time | Rec1_Calls | Rec2_Time | Rec2_Calls")
print("-" * 65)

for n in input_sizes:
    
    # Recurrence 1 
    calls_1 = 0
    start = time.perf_counter()
    recurrence_1(n)
    time_1 = time.perf_counter() - start
    
    # Recurrence 2 
    calls_2 = 0
    start = time.perf_counter()
    recurrence_2(n)
    time_2 = time.perf_counter() - start
    
    print(f"{n} | "
          f"{time_1:.6f} | {calls_1} | "
          f"{time_2:.6f} | {calls_2}")
