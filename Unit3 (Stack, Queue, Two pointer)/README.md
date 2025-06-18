# Unit 3 Cheatsheet

## Overview

Here is a helpful cheatsheet outlining common syntax and concepts that will help you in your problem solving journey! Use this as a reference while you solve the breakout problems for Unit 3. This is not an exhaustive list of all data structures, algorithmic techniques, and syntax you may encounter; it only covers the most critical concepts needed to ace Unit 3. In addition to the material below, you are expected to know any required concepts from previous units. You may also find advanced concepts and bonus concepts included at the bottom of this page helpful for solving problem set questions, but you are not required to know them for the unit assessment.

---

## Standard Concepts

### Stacks

Stacks are a special type of list where elements are always added and removed in a certain order. Stacks follow the **Last In, First Out (LIFO)** principle, which means that the last element added to the stack will be the first element to be removed.

Imagine the stack data structure as a stack of plates. When we add a new plate (element) to the stack, the plate gets added to the top of the existing stack. When we want to remove a plate from the stack, the plate that is easiest to remove is the plate on the top of the stack.

- **Push**: Adding a new element to the stack
- **Pop**: Removing an element from the stack

```
Stack Visualization:
┌─────────┐
│    3    │ ← Top (Last In, First Out)
├─────────┤
│    2    │
├─────────┤
│    1    │ ← Bottom
└─────────┘
```

#### Stack Implementation

Stacks can easily be implemented using the built-in list data type in Python and built-in `append()` and `pop()` methods.

```python
stack = []

# Push new items onto the top of the stack
stack.append(1)
stack.append(2)

# Pop an item off the top of the stack
popped_item = stack.pop()

print(popped_item)  # Prints: 2
print(stack)        # Prints: [1]
```

`append()` and `pop()` are both very fast functions (O(1) time complexity for those familiar with Big O), so using a normal Python list to implement a stack is an extremely efficient way to implement a stack.

#### When to Use a Stack

What are some common signs a problem could be solved using a stack?

1. **Reversing Data**: Reversing the order of a sequence such as a list or string
   - Example: Reverse String

2. **Balancing Symbols**: Checking for or managing pairs of symbols like parentheses, brackets, or braces
   - Example: Valid Parentheses

3. **Backtracking**: Exploring multiple paths or states, returning to previous states
   - Example: Depth First Search (DFS) algorithms

4. **Expression Evaluation**: Evaluating or converting expressions, particularly in postfix or infix form
   - Example: Reverse Polish Notation

---

### Queues

Queues are a special type of list where elements are always added and removed in a certain order. Queues follow the **First In, First Out (FIFO)** principle, which means that the first element added to the queue will be the first element to be removed.

The term 'queue' comes from the British meaning of the word queue: a line of waiting people. Queue data structures follow the same logic as queues of real people! New elements are always appended to the end of a queue and removed from the beginning of the queue.

```
Queue Visualization:
┌─────────────────────────────────────┐
│  1  │  2  │  3  │  4  │  5  │       │
│     │     │     │     │     │       │
└─────────────────────────────────────┘
  ↑                           ↑
Front                       Rear
(Dequeue)                (Enqueue)
```

#### Queue Implementation

In Python, we use the `deque` class to create a new Queue.

```python
# 1. Import the deque module
from collections import deque 

# 2. Initialize a new deque object (a new queue)
queue = deque()

# 3. Add a new element, 1, to the end (right side) of the queue
queue.append(1)

# 4. Remove an element from the beginning (left side) of the queue
removed_elt = queue.popleft()
print(removed_elt)  # Prints 1
```

Alternative approach (adding to left, removing from right):

```python
from collections import deque 

queue = deque()

# Add a new element to the left side of the queue
queue.appendleft(1)

# Remove an element from the right side of the queue
removed_elt = queue.pop()
print(removed_elt)  # Prints 1
```

#### When to Use a Queue

What are some common signs a problem could be solved using a queue?

1. **Processing Items**: Processing items in sequence in the order they arrive
   - Example: Number of Recent Calls

2. **Breadth First Search (BFS)**: Exploring trees and graphs level by level
   - Example: Level Order Traversal of a Binary Tree

3. **Round-Robin Scheduling**: Processing tasks in a cyclic order
   - Example: Task Scheduler problem

---

### Two Pointer

The two-pointer approach is a common technique in which we initialize two pointer variables to track different indices or places in a list or string and move them to new indices based on certain conditions.

#### Opposite Direction Pointers

The most common variation where one pointer starts at the beginning and another at the end, moving towards each other.

```
Initial State:
┌─────┬─────┬─────┬─────┬─────┬─────┐
│  1  │  2  │  3  │  4  │  5  │  6  │
└─────┴─────┴─────┴─────┴─────┴─────┘
  ↑                               ↑
left                            right
```

```python
left_pointer = 0
right_pointer = len(word) - 1
while left_pointer < right_pointer:
    # Process elements at both pointers
    left_pointer += 1
    right_pointer -= 1
```

#### Same Direction Pointers

Two pointers starting at the beginning of different lists or the same list, moving in the same direction.

```
List 1: [1, 4, 5]
         ↑
      pointer1

List 2: [2, 3, 6]
         ↑
      pointer2
```

```python
nums1_pointer = 0
nums2_pointer = 0

while nums1_pointer < len(nums1) and nums2_pointer < len(nums2):
    if condition:
        # Process nums1[nums1_pointer]
        nums1_pointer += 1
    else:
        # Process nums2[nums2_pointer]
        nums2_pointer += 1
```

#### When to Use Two-Pointer Technique

1. **Data Structure**: Most commonly applied to strings, arrays, and linked lists
2. **Reducing Nested Loops**: Improving brute force solutions that use multiple for loops
3. **Searching for Pairs or Triplets**: Finding pairs/triplets in sorted arrays
4. **In Place Operations**: Performing operations without extra data structures
5. **Comparing Opposite Ends**: Processing elements from both ends of a sequence
6. **Partitioning Problems**: Dividing data into multiple parts

---

### Helper Functions

Helper functions are functions we write to implement a subtask of our primary task. They help keep our main function shorter and easier to read.

```python
# Example: Calculating a Bill Total

# Helper Function: Calculate the price of one item
def calculate_price(item_price, quantity):
    return item_price * quantity

# Primary Function: Calculate total cost of bill
def calculate_total(bill):
    total = 0
    for item_price, quantity in bill.items():
        # Call helper function
        total += calculate_price(item_price, quantity)
    return total
```

Helper functions help us follow the **Single Responsibility Principle (SRP)** which says that a function should perform only a single task or action.

---

## Python Syntax

### Unpacking

Unpacking is a method of assigning multiple variables at once, commonly used with the 2-pointer approach.

```python
# Assign multiple variables at once
a, b = 1, 2

# Swapping pointer indices
pointer_one, pointer_two = pointer_two, pointer_one

# Swapping values in a list
nums[pointer_one], nums[pointer_two] = nums[pointer_two], nums[pointer_one]

# Unpacking from nested lists
inventory = [["apples", 3], ["carrots", 5]]
[[item, quantity], [item2, quantity2]] = inventory
```

### Inner Functions

Inner Functions (nested functions) are functions defined inside another function.

```python
# Outer function
def print_sum(x, y):
    
    # Inner function
    def get_sum():
        return x + y

    total = get_sum()
    print(f"{x} + {y} is {total}")

print_sum(1, 2)  # Prints: 1 + 2 is 3
```

**Key Points:**
- Inner functions have access to variables and parameters of the outer function
- They are only available within the scope of the outer function
- Commonly used for helper functions specific to the main function

```python
def total_sum_of_digits(numbers):
    # Inner function to calculate the sum of digits of a single number
    def sum_of_digits(n):
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total

    # Main function logic
    total_sum = 0
    for number in numbers:
        total_sum += sum_of_digits(number)
    
    return total_sum
```

---

## Advanced Concepts

There are no extra advanced syntax or concepts for this unit! 😎 The advanced component comes from the difficulty of the problems!

---

## Bonus Syntax & Concepts

The following concepts are nice to know and may improve your code readability or help you solve certain problems more easily and efficiently. However, they are not required to solve any of the problems in this unit.

### Diving Deeper: Stacks vs Queues

**Stacks and Queues Comparison:**

| Aspect | Stack (LIFO) | Queue (FIFO) |
|--------|--------------|--------------|
| Insertion | Top (Push) | Rear (Enqueue) |
| Removal | Top (Pop) | Front (Dequeue) |
| Common Solutions | Recursive | Iterative (while loops) |
| Use Cases | Backtracking, Expression Evaluation | BFS, Task Scheduling |

**Implementation Relationship:**
- Stack problems often implement recursive solutions (using the call stack)
- Queue problems generally use iterative solutions with while loops
- Stack problems can always be solved iteratively as well

```python
# Reverse a string using iterative stack solution
def reverse_string_iterative(s):
    stack = []
    
    # Push all characters onto the stack
    for char in s:
        stack.append(char)
    
    reversed_string = ""
    
    # Pop all characters and append to result
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Reverse a string using recursive solution
def reverse_string_recursive(s):
    # Base case
    if len(s) <= 1:
        return s
    
    # Recursive case
    return reverse_string_recursive(s[1:]) + s[0]
```

---

*This cheatsheet covers the essential concepts for Unit 3. Practice with these data structures and techniques to build your problem-solving skills!*