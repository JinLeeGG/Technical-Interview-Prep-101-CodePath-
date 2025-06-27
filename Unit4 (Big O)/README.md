# Unit 4 Cheatsheet - Asymptotic Analysis & Big O

## Overview

This cheatsheet outlines common syntax and concepts for asymptotic analysis and Big O notation. Use this as reference when solving Unit 4 problems. This covers the most critical concepts needed, though you're expected to know required concepts from previous units as well.

⚠️ **Course Scope**: For this course, evaluate **worst case performance** unless otherwise stated. For Unit 3 standard exam, only constant, linear, and quadratic algorithms are in scope.

---

## Standard Concepts

### What is Asymptotic Analysis?

Asymptotic Analysis is a method for measuring the execution time and memory usage of algorithms as input size grows. It helps us:

- Write efficient algorithms that execute quickly on large datasets (1M+ items)
- Minimize computer memory usage
- Compare different solutions and select optimal ones
- Judge if an algorithm can solve problems within reasonable time/space constraints

**Two Components:**
1. **Time Complexity** - How execution time changes as input size changes
2. **Space Complexity** - How memory usage changes as input size changes

---

## Big O Notation Reference

Big O uses the syntax `O(...)` where the expression inside describes the relationship between input size and algorithm complexity.

| Complexity | Name | Definition | Example Use Cases |
|------------|------|------------|-------------------|
| `O(1)` | Constant | Same time regardless of input size | Array access, hash table lookup |
| `O(log n)` | Logarithmic | Grows proportional to log₂(n) | Binary search, balanced tree operations |
| `O(n)` | Linear | Grows directly proportional to input | Single loop, linear search |
| `O(n log n)` | Log Linear | Input size × log of input size | Merge sort, heap sort |
| `O(n²)` | Quadratic | Proportional to input size squared | Nested loops, bubble sort |
| `O(2ⁿ)` | Exponential | Doubles with each input increase | Recursive fibonacci, subset generation |

### Performance Ranking (Best to Worst)
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
```

---

## Time Complexity Examples

### O(1) - Constant Time
```python
def add_from_1_to_n(n):
    return (n * (n + 1)) / 2  # Same operations regardless of n

def get_first_element(arr):
    return arr[0]  # Always one operation
```

### O(n) - Linear Time
```python
def add_from_1_to_n(n):
    total = 0
    for i in range(1, n + 1):  # Loop runs n times
        total += i
    return total

def find_max(arr):
    max_val = arr[0]
    for num in arr:  # Single pass through array
        if num > max_val:
            max_val = num
    return max_val
```

### O(n²) - Quadratic Time
```python
def duplicates_within_k(numbers, k):
    lst_length = len(numbers)
    
    for i in range(lst_length):        # Outer loop: n times
        j = i + 1
        dist_remaining = k
        while dist_remaining > 0 and j < lst_length:  # Inner loop: up to n times
            if numbers[i] == numbers[j]:
                return True
            j += 1
            dist_remaining -= 1
    return False

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # Outer loop
        for j in range(0, n-i-1):  # Inner loop
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

---

## Space Complexity Examples

### O(1) - Constant Space
```python
def sum_array(arr):
    total = 0    # Single variable
    for num in arr:
        total += num  # Reusing same variable
    return total
```

### O(n) - Linear Space
```python
def copy_array(arr):
    copy = []           # New array of size n
    for num in arr:
        copy.append(num)
    return copy

def reverse_string(s):
    return s[::-1]  # Creates new string of size n
```

### O(n²) - Quadratic Space
```python
def init_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        for col in range(n):        # n×n matrix = n² space
            matrix[row].append(None)
    return matrix

def all_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):   # n² pairs stored
            pairs.append((arr[i], arr[j]))
    return pairs
```

---

## Built-In Function Complexities

| Function | Time Complexity | Notes |
|----------|----------------|-------|
| `len()` | O(1) | Length is stored |
| `sequence[idx]` | O(1) | Direct access |
| `sequence[start:end]` | O(k) | k = slice length |
| `sequence.sort()` | O(n log n) | Timsort algorithm |
| `sorted(sequence)` | O(n log n) | Creates new sorted sequence |
| `sequence.copy()` | O(n) | Shallow copy |
| `list.append()` | O(1)* | Amortized constant |
| `list.pop()` | O(1) | From end only |
| `list.insert()` | O(n) | May shift elements |
| `dict.get()` | O(1)* | Average case |
| `dict.pop()` | O(1)* | Average case |
| `"".join(list)` | O(n) | n = total character count |

*Amortized or average case

---

## Big O Rules & Tips

### Simplification Rules
1. **Drop constants**: `O(2n)` → `O(n)`
2. **Drop lower-order terms**: `O(n² + n)` → `O(n²)`
3. **Sequential operations add**: `O(n) + O(m)` → `O(n + m)`
4. **Nested operations multiply**: `O(n) × O(m)` → `O(n × m)`

### Analysis Tips
- Focus on the **dominant term** for large inputs
- Consider **worst-case** unless specified otherwise
- Don't count input space in space complexity
- Account for helper function complexities
- Use separate variables for multiple inputs of different sizes

---

## Advanced Concepts

### Multiple Variables
When functions have multiple inputs affecting complexity:

```python
def init_matrix(rows, columns):
    matrix = []
    for r in range(rows):           # m iterations
        matrix.append([])
        for c in range(columns):    # n iterations
            matrix[r].append(None)
    return matrix
# Time: O(m × n), Space: O(m × n)
```

### Amortized Analysis
Some operations are expensive occasionally but cheap on average:

```python
# Dynamic array (list) append
# - Usually O(1) 
# - Occasionally O(n) when resizing
# - Amortized O(1) over many operations
```

---

## Common Patterns & Algorithms

### Searching Algorithms
```python
# Linear Search: O(n) time, O(1) space
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Binary Search: O(log n) time, O(1) space
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Sorting Algorithms
| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |

---

## Practice Problems Framework

When analyzing complexity:

1. **Identify the input size** (usually n)
2. **Count the operations** in loops and recursive calls
3. **Consider nested structures** (multiply complexities)
4. **Account for built-in functions** used
5. **Simplify using Big O rules**
6. **State your assumptions** clearly

### Example Analysis Process:
```python
def example_function(arr):
    # Step 1: n = len(arr)
    result = []                    # O(1) space
    
    for i in range(len(arr)):      # O(n) iterations
        temp = []                  # O(1) space per iteration
        for j in range(i):         # O(i) iterations, worst case O(n)
            temp.append(arr[j])    # O(1) per append
        result.append(temp[:])     # O(i) for slice, worst case O(n)
    
    return result

# Time: O(n) × O(n) × O(n) = O(n³)
# Space: O(n²) for result storage
```

---

## Quick Reference Formulas

### Loop Analysis
- Single loop over n elements: **O(n)**
- Nested loops (both n): **O(n²)**
- Loop reducing problem by half each time: **O(log n)**
- Loop with inner binary search: **O(n log n)**

### Recursive Analysis
Use the recurrence relation:
- `T(n) = T(n/2) + O(1)` → **O(log n)** (binary search)
- `T(n) = 2T(n/2) + O(n)` → **O(n log n)** (merge sort)
- `T(n) = 2T(n-1) + O(1)` → **O(2ⁿ)** (naive fibonacci)

