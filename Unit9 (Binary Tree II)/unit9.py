
from collections import deque
import collections

class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


# Problem 1: Merging Cookie Orders
# You run a local bakery and are given the roots of two binary trees order1 and order2 where each node in the binary tree represents the number of a certain cookie type the customer has ordered. To maximize efficiency, you want to bake enough of each type of cookie for both orders together.

# Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders, imagine that when place one tree on top of the other, some nodes of the two trees are overlapped while others are not. If two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the not None node will be used as the node of the new tree.

# Start the merging process from the root of both orders.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.


def merge_orders(order1, order2):
    # base case
    if not order1:
        return order2 

    if not order2:
        return order1

    merged = TreeNode(order1.val + order2.val)

    # recursive case 
    merged.left = merge_orders(order1.left, order2.left)
    merged.right = merge_orders(order1.right, order2.right)

    return merged

"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
# print_tree(merge_orders(order1, order2))




# Problem 2: Croquembouche
# You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

# Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, that prints a list of the flavors (vals) of each cream puff in level order (i.e., from left to right, level by level).

# Note: The build_tree() and print_tree() functions both use variations of a level order traversal. To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


def print_design(design):
    
    flavors = []

    queue = collections.deque([design])

    while queue:

        node = queue.popleft()
        flavors.append(node.val)

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)

    print(flavors)

# Example Usage:

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))

print_design(croquembouche)

# Example Output:

# ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']



# Problem 3: Maximum Tiers in Cake
# You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different section of your cake, return the maximum number of tiers in your cake.

# The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    # Base Case: (when leaf is None -> depth = 0)
    if not cake:
        return 0

    # Recursive Case: (non-leaf node -> call children and add 1)
    return max(max_tiers(cake.left), max_tiers(cake.right)) + 1

# Example Usage:

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

# print(max_tiers(cake))

# Example Output:

# 3


# Problem 4: Maximum Tiers in Cake II
# If you solved max_tiers() in the previous problem using a depth first search approach, reimplement your solution using a breadth first search approach. If you implemented it using a breadth first search approach, use a depth first search approach.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    
    queue = collections.deque([cake])

    # counter 
    result = 0 

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result += 1
    return result

# Example Usage:
# [chocolate (1)]
# [vanilla (2), strawberry (2)]
"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

# print(max_tiers(cake))
# Example Output:

# 3


# Problem 5: Can Fulfill Order
# At your bakery, you organize your current stock of baked goods in a binary tree with root inventory where each node represents the quantity of a baked good in your bakery. A customer comes in wanting a random assortment of baked goods of quantity order_size. Given the root inventory and integer order_size, return True if you can fulfill the order and False otherwise. You can fulfill the order if the tree has a root-to-leaf path such that adding up all the values along the path equals order_size.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def can_fulfill_order(inventory, order_size):
    pass

# Example Usage:

"""
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   
"""

# Using build_tree() function included at top of the page
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))

# Example Output:

# True
# Example 1 Explanation: 5 + 4 + 11 + 2 = 22

# False