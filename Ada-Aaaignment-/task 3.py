# --------------------------------------------
# Recursion and Recurrence Validation
# --------------------------------------------

import time

# --------------------------------------------
# 1. Factorial (Recursive)
# --------------------------------------------

fact_calls = 0

def factorial(n):
    global fact_calls
    fact_calls += 1
    
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# --------------------------------------------
# 2. Fibonacci (Naïve Recursive)
# --------------------------------------------

fib_calls = 0

def fibonacci_recursive(n):
    global fib_calls
    fib_calls += 1
    
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# --------------------------------------------
# 3. Fibonacci (Dynamic Programming - Memoization)
# --------------------------------------------

fib_dp_calls = 0

def fibonacci_dp(n, memo=None):
    global fib_dp_calls
    fib_dp_calls += 1
    
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = n
        return n
    
    memo[n] = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    return memo[n]


# --------------------------------------------
# Experiment
# --------------------------------------------

input_sizes = [5, 10, 20, 30]

print("n | Fact_Time | Fact_Calls | FibRec_Time | FibRec_Calls | FibDP_Time | FibDP_Calls")
print("-" * 85)

for n in input_sizes:
    
    # Factorial
    fact_calls = 0
    start = time.perf_counter()
    factorial(n)
    fact_time = time.perf_counter() - start
    
    # Fibonacci Recursive
    fib_calls = 0
    start = time.perf_counter()
    fibonacci_recursive(n)
    fib_time = time.perf_counter() - start
    
    # Fibonacci DP
    fib_dp_calls = 0
    start = time.perf_counter()
    fibonacci_dp(n)
    fib_dp_time = time.perf_counter() - start
    
    print(f"{n} | "
          f"{fact_time:.6f} | {fact_calls} | "
          f"{fib_time:.6f} | {fib_calls} | "
          f"{fib_dp_time:.6f} | {fib_dp_calls}")
