# -----------------------------------------
# Best, Average, Worst Case Analysis
# Linear Search vs Binary Search
# -----------------------------------------

import random
import time
import matplotlib.pyplot as plt

# -----------------------------------------
# Search Algorithm Implementations
# -----------------------------------------

# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Binary Search (array must be sorted)
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1



# Experiment Setup


input_sizes = [100, 500, 1000, 5000]

linear_best = []
linear_avg = []
linear_worst = []

binary_best = []
binary_avg = []
binary_worst = []

for n in input_sizes:
    
    # Generate sorted random array
    arr = sorted(random.sample(range(n * 10), n))
    
    # -----------------------------
    # Linear Search Cases
    # -----------------------------
    
    # Best Case (element at first position)
    start = time.time()
    linear_search(arr, arr[0])
    linear_best.append(time.time() - start)
    
    # Average Case (element in middle)
    start = time.time()
    linear_search(arr, arr[n // 2])
    linear_avg.append(time.time() - start)
    
    # Worst Case (element not present)
    start = time.time()
    linear_search(arr, -1)
    linear_worst.append(time.time() - start)
    
    
    # -----------------------------
    # Binary Search Cases
    # -----------------------------
    
    # Best Case (element at middle)
    start = time.time()
    binary_search(arr, arr[n // 2])
    binary_best.append(time.time() - start)
    
    # Average Case (random element)
    start = time.time()
    binary_search(arr, arr[random.randint(0, n - 1)])
    binary_avg.append(time.time() - start)
    
    # Worst Case (element not present)
    start = time.time()
    binary_search(arr, -1)
    binary_worst.append(time.time() - start)


# -----------------------------------------
# Plot Linear Search
# -----------------------------------------

plt.figure()
plt.plot(input_sizes, linear_best)
plt.plot(input_sizes, linear_avg)
plt.plot(input_sizes, linear_worst)
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Linear Search - Best, Average, Worst Case")
plt.show()


# -----------------------------------------
# Plot Binary Search
# -----------------------------------------

plt.figure()
plt.plot(input_sizes, binary_best)
plt.plot(input_sizes, binary_avg)
plt.plot(input_sizes, binary_worst)
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Binary Search - Best, Average, Worst Case")
plt.show()


# -----------------------------------------
# Observations
# -----------------------------------------

"""
Observations:

1. Linear Search:
   - Best Case: O(1) (element found at first position)
   - Average Case: O(n)
   - Worst Case: O(n)
   Time increases linearly with input size.

2. Binary Search:
   - Best Case: O(1) (element at middle)
   - Average Case: O(log n)
   - Worst Case: O(log n)
   Time increases very slowly compared to linear search.

Conclusion:
Binary Search is much more efficient for large datasets,
but it requires the array to be sorted.
"""
