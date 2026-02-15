# Ada-Assignment
# analysis.ipynb
TASK 1: Best, Average & Worst Case
(Linear Search vs Binary Search)
 Overview

You implemented:

Linear Search

Binary Search

You:

Generated random sorted arrays

Measured execution time for:

Best case

Average case

Worst case

Plotted comparison graphs
 Objective

To understand:

Linear Search → O(n)

Binary Search → O(log n)

How performance changes with input size

 How to Execute
Step 1:

Install required libraries (if needed):

pip install matplotlib

Step 2:

Save the code as:

search_analysis.py

Step 3:

Run:

python search_analysis.py

Output:

Two graphs:

Linear Search comparison

Binary Search comparison

Time measurements printed

 TASK 2: Recursion & Recurrence Validation
(Factorial & Fibonacci Comparison)
Overview

You implemented:

Recursive Factorial

Naïve Recursive Fibonacci

Fibonacci using Dynamic Programming

You:

Counted function calls

Measured execution time

Compared exponential vs linear growth

 Objective

To observe:

Factorial → O(n)

Fibonacci Recursive → O(2ⁿ)

Fibonacci DP → O(n)

How to Execute
Step 1:

Save file as:

recursion_validation.py

Step 2:

Run:

python recursion_validation.py

Output:

Printed comparison table

Clear difference in call counts

Time comparison

TASK 3: Solving Recurrences Through Code
(T(n) = T(n/2)+n and 2T(n/2)+n)
 Overview

You implemented recursive functions matching:

T(n) = T(n/2) + n → O(n)

T(n) = 2T(n/2) + n → O(n log n)

You:

Counted recursive calls

Measured execution time

Validated using Master Theorem

 Objective

To experimentally verify:

Linear vs n log n growth

How to Execute
Step 1:

Save as:

recurrence_analysis.py

Step 2:

Run:

python recurrence_analysis.py

Output:

Time measurements

Call counts

Growth validation

TASK 4: Time Complexity Visualization
(O(1), O(n), O(n²), O(log n))
 Overview

You implemented functions for:

Constant Time

Linear Time

Quadratic Time

Logarithmic Time

You:

Measured execution time

Plotted input size vs time

Observed growth patterns

 Objective

To visually compare algorithm complexity behavior.

 How to Execute
Step 1:

Install matplotlib (if not installed):

pip install matplotlib

Step 2:

Save as:

complexity_visualization.py

Step 3:

Run:

python complexity_visualization.py

Output:

4 separate graphs

Clear growth comparison

