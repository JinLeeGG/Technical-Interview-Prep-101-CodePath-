# Unit 7 - Recursion & Divide & Conquer (2025/07/15)

## Overview
This unit covers recursion, divide & conquer algorithms, and time complexity analysis. These are fundamental concepts for solving complex problems efficiently.

## Standard Concepts

### Recursion Fundamentals

**Definition**: Recursion is the process of a function calling itself to solve a problem by breaking it down into smaller, similar subproblems.

#### Iteration vs Recursion
- **Iteration**: Bottom-up approach, starts with smallest subproblem and builds up
- **Recursion**: Top-down approach, breaks large problem into smaller subproblems

```python
# Iterative Approach
def count_iterative(num):
    i = 1
    while i <= num:
        print(f"Count {i}!")
        i += 1

# Recursive Approach  
def count_recursive(num):
    print(f"Count {num}!")
    if num == 1:
        return
    else:
        count_recursive(num - 1)
```

#### Building Recursive Functions

Every recursive function needs:

1. **Base Case**: End condition that stops recursion
2. **Recursive Case**: Function calls itself with modified input

```python
def count_recursive(num):
    # Action to repeat
    print(f"Count {num}!")
    
    # Base Case
    if num == 1:
        return
    
    # Recursive Case
    else:
        count_recursive(num - 1)
```

#### Multiple Base Cases

```python
def is_odd(n):
    # Base Case 1: n is 0 (not odd)
    if n == 0:
        return False
    
    # Base Case 2: n is 1 (odd)
    if n == 1:
        return True
    
    # Recursive case
    else:
        return is_odd(n - 2)
```

#### Multiple Recursive Cases

```python
def count_evens(lst):
    # Base case
    if not lst:
        return 0
    
    # Recursive Case 1: first element is even
    if lst[0] % 2 == 0:
        return 1 + count_evens(lst[1:])
    
    # Recursive Case 2: first element is odd
    else:
        return count_evens(lst[1:])
```

#### Return Statement as Accumulator

In recursive functions, the return statement acts as the accumulator variable:

```python
# Return combines current result with recursive call result
return 1 + count_evens(lst[1:])
```

### Recursive Driver and Helper Functions

When you need to pass extra data to recursive calls, use a helper function:

```python
def partition_evens_odds(lst):
    # Driver function - calls helper with initial values
    return recurse_partition(lst, [], [])

def recurse_partition(lst, evens, odds):
    # Helper function - does the recursive work
    if not lst:
        return evens, odds
    
    if lst[0] % 2 == 0:
        evens.append(lst[0])
    else:
        odds.append(lst[0])
    
    return recurse_partition(lst[1:], evens, odds)
```

**Why Use Helper Functions?**
- Driver function provides clean interface for users
- Helper function handles the recursive logic with additional parameters
- Avoids forcing users to pass initial values

## Divide & Conquer Algorithms

**Definition**: Algorithmic technique that solves problems by:
1. **Divide**: Break problem into smaller subproblems
2. **Conquer**: Solve each subproblem (often recursively)
3. **Combine**: Merge solutions to solve the original problem

### Binary Search

Classic divide & conquer algorithm for finding a target in a sorted list.

**Time Complexity**: O(log n)

```python
def binary_search(numbers, value):
    low = 0
    high = len(numbers) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if numbers[mid] > value:
            high = mid - 1
        elif numbers[mid] < value:
            low = mid + 1
        else:
            return mid
    
    return None
```

**How it works**:
- Compare target with middle element
- Eliminate half of the remaining search space
- Repeat until found or search space is empty

### Merge Sort

Efficient sorting algorithm using divide & conquer.

**Time Complexity**: O(n log n)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Conquer & Combine
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

## Time Complexity Analysis

### Logarithmic Time Complexity - O(log n)

**Characteristics**:
- Input size is divided by constant factor each iteration
- Very efficient - grows slowly as input increases
- Common in divide & conquer algorithms

**Example**: Binary Search
- Each iteration eliminates half the remaining elements
- For input size n, maximum iterations ≈ log₂(n)

| Input Size (n) | Max Iterations |
|---------------|----------------|
| 8             | 3              |
| 16            | 4              |
| 32            | 5              |
| 64            | 6              |

### Log-Linear Time Complexity - O(n log n)

**Characteristics**:
- Combines linear pass through data (n) with logarithmic factor (log n)
- Common in efficient sorting algorithms
- More efficient than O(n²) but less than O(n)

**Example**: Merge Sort
- **Dividing**: O(log n) - number of times array is split
- **Merging**: O(n) - comparing elements during merge
- **Total**: O(n) × O(log n) = O(n log n)

### Exponential Time Complexity - O(2ⁿ)

**Characteristics**:
- Runtime doubles with each addition to input size
- Very inefficient - avoid when possible
- Common in naive recursive solutions

**Example**: Naive Fibonacci
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

Each call creates two more calls, leading to exponential growth.

## The Call Stack

### How It Works
- Stack data structure tracks function calls
- New function calls get added to top of stack
- Functions execute in LIFO (Last In, First Out) order
- When function completes, it's removed from stack

### Call Stack Example
```python
def function_c():
    print("I'm Function C!")

def function_b():
    print("I'm Function B!")
    function_c()
    print("Function B is done!")

def function_a():
    print("I'm Function A!")
    function_b()
    print("Function A is done!")
```

**Execution Order**:
1. function_a() added to stack
2. function_b() added to stack
3. function_c() added to stack
4. function_c() executes and is removed
5. function_b() completes and is removed
6. function_a() completes and is removed

### Recursion and Space Complexity

**Key Points**:
- Each recursive call uses memory on the call stack
- Deep recursion can lead to stack overflow
- Space complexity often matches the maximum depth of recursion

**Example**: For a recursive function that calls itself n times:
- **Space Complexity**: O(n) due to call stack usage
- Each function call remains on stack until base case is reached

## Summary

### When to Use Recursion
- ✅ Problem can be broken into similar subproblems
- ✅ Clear base case exists
- ✅ Recursive solution is more intuitive than iterative
- ❌ Avoid for simple iterations (use loops instead)
- ❌ Avoid if it leads to exponential time complexity

### Common Patterns
1. **List Processing**: Process first element, recurse on rest
2. **Tree Traversal**: Process current node, recurse on children
3. **Divide & Conquer**: Split problem, solve parts, combine results

### Time Complexity Quick Reference
- **O(log n)**: Binary search, balanced tree operations
- **O(n log n)**: Merge sort, heap sort
- **O(2ⁿ)**: Naive recursive solutions (avoid!)
- **O(n)**: Linear recursion (single recursive call per iteration)

### Best Practices
- Always define clear base cases
- Ensure recursive calls move toward base case
- Consider iterative solutions for simple problems
- Use helper functions when additional parameters needed
- Be mindful of space complexity due to call stack usage

