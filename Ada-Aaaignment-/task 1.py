# O(1) - Constant Time

def constant_time(n):
    return n * 2   # Executes only once

# Test
n = 1000
print("Result:", constant_time(n))

# O(n) - Linear Time

def linear_time(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Test
n = 1000
print("Result:", linear_time(n))

# O(n^2) - Quadratic Time

def quadratic_time(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total

# Test
n = 500
print("Result:", quadratic_time(n))

# O(log n) - Logarithmic Time

def logarithmic_time(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

# Test
n = 1000
print("Result:", logarithmic_time(n))

import time

input_sizes = [10, 100, 500, 1000]

for n in input_sizes:
    start = time.time()
    linear_time(n)
    end = time.time()
    print(f"Input Size: {n}, Execution Time: {end - start} seconds")
