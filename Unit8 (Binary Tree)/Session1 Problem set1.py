# Problem 1: Grafting Apples
# You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

# The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

    #          Trunk
    #       /         \
    #   Mcintosh   Granny Smith
    #   /     \       /     \
    # Fuji   Opal   Crab   Gala

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

# creating tree
root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")
root.left.left = TreeNode("Fiji")
root.right.right = TreeNode("Gala")
root.left.right = TreeNode("Opal")
root.right.left = TreeNode("Crab")


# Example Usage:

# Using print_tree() included at the top of this page
print_tree(root)

# Example Output:

['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']



# Problem 2: Calculating Yield
# You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. 
# Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

# Leaf nodes have an integer value.
# The root has a string value of either "+", "-", "*", or "-".
# The yield of a the tree is calculated by applying the mathematical operation to the two children.

# Return the result of evaluating the root node.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution 
# has the stated time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if root.val == '+':
        return root.left.val + root.right.val
    elif root.val == '-':
        return root.left.val - root.right.val
    elif root.val == '*':
        return root.left.val * root.right.val
    else:
        return root.left.val / root.right.val


# Example Usage:

"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))

# Example Output:
# 12


# Problem 3: Ivy Cutting
# You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using 
# the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path 
# from the root node to the rightmost leaf node.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your
# solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    vine_list = []
    while root:
        vine_list.append(root.val)
        root = root.right

    return vine_list

# Example Usage:

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))

# Example Output:

# ['Root', 'Node2', 'Leaf3']
# ['Root']





# Problem 4: Ivy Cutting II
# If you implemented right_vine() iteratively in the previous problem, implement it recursively. 
# If you implemented it recursively, implement it iteratively.

# Evaluate the time complexity of your function. 
# Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
# Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    # base case
    vine_list = []
    return vine_helper(root, vine_list)

def vine_helper(root, tracker):
    tracker.append(root.val)
    if not root.right:
        return tracker

    vine_helper(root.right, tracker)
    return tracker
# Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
# Example Output:

# ['Root', 'Node2', 'Leaf3']
# ['Root']




# Problem 5: Count the Tree Leaves
# You've grown an oak tree from a tiny little acorn and it's finally sprouting leaves! Given the root of a binary tree representing your oak tree, count the number of leaf nodes in the tree. A leaf node is a node that does not have any children.

# Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root):

    if not root:
        return 0

    # base case
    if not root.right and not root.left:
        return 1

    # recursive case
    return count_leaves(root.left) + count_leaves(root.right)


# Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))
# Example Output:

# 3
# 1


# Problem 6: Pruning Plans
# You have a large overgrown Magnolia tree that's in desperate need of some pruning. 
# Before you can prune the tree, you need to do a full survey of the tree to evaluate which sections need to be pruned.

# Given the root of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. 
# In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. 
# Postorder traversals are often used when deleting nodes from a tree.

# Evaluate the time complexity of your function. 
# Define your variables and provide a rationale for why you believe your solution has the stated time complexity. 
# Assume the input tree is balanced when calculating time complexity.

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    lst = []
    
    pass

def survey_helper(root, lst):
    if root.right:
        lst.append(root.right.val)
    if root.left:
        lst.append(root.left.val)
    
    survey_helper(root.right)
    survey_helper(root.left)
    lst.append(root.val)
    return lst
# Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

# Example Output:

# ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]