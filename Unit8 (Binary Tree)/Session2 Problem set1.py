from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
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

# Problem 1: Monstera Madness
# Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves that have an odd number of splits.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
         
def count_odd_splits(root):

    # base case: when we do not have more nodes to search, return 0

    if not root:
        return 0
    
    counter = 0

    if root.val % 2 != 0:
        counter += 1
    
    # recursive case: search left, right node for odd number 

    return counter + count_odd_splits(root.left) + count_odd_splits(root.right)

    # 0 + 1 
 
# Example Usage:

"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))

# Example Output:

# 3
# 0



# Problem 2: Flower Finding
# You are looking to buy a new flower plant for your 
# garden. The nursery you visit stores its inventory in a 
# binary search tree (BST) where each node represents a 
# plant in the store. The plants are organized according 
# to their names (vals) in alphabetical order in the BST.

# Given the root of the binary search tree inventory 
# and a target flower name, write a function find_flower()
#  that returns True if the flower is present in the 
# garden and False otherwise.

# Evaluate the time complexity of your function. 
# Define your variables and provide a rationale for 
# why you believe your solution has the stated time
# complexity. Assume the input tree is balanced when 
# calculating time complexity.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    #base case: if theres a root
    if not inventory:
        return False

    isFlower = False

    if inventory.val == name:
        isFlower = True


    return isFlower or find_flower(inventory.left, name) or find_flower(inventory.right, name)
    #find the "name" in "inventory"

    #check if the name of the current flower matches "name"
    
    #return find_flower(inventory.right) 



# Example Usage:

"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

# Example Output:

# True
# False


# Problem 3: Flower Finding II

# Consider the following function non_bst_find_flower() which accepts the root of a binary tree inventory and a flower name, and returns True if a flower (node) with name exists in the binary tree. Unlike the previous problem, this tree is not a binary search tree.

# Compare your solution to find_flower() in Problem 2 to the following solution. Discuss with your group: How is the code different? Why?

# What is the time complexity of non_bst_find_flower()? How does it compare to the time complexity of find_flower() in Problem 2?

# How would the time complexity of find_flower() from Problem 2 change if the tree inventory was not balanced?

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

# Example Usage:

"""
         Daisy
        /    \
      Lily   Tulip
     /  \       \
  Rose  Violet  Lilac
"""

# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower"))  

# Example Output:

# True
# False