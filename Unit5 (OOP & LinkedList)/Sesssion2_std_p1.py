# Problem 1: Mutual Friends
# In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.

# Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, and returns a list with the name of all friends the current villager and new_contact have in common.

# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.friends = []

#     def get_mutuals(self, new_contact):
#         lst = []
#         for villager in new_contact.friends:
#             if villager in self.friends:
#                 lst.append(villager.name)
        
#         return lst

# Example Usage:

# bob = Villager("Bob", "Cat", "pthhhpth")
# marshal = Villager("Marshal", "Squirrel", "sulky")
# ankha = Villager("Ankha", "Cat", "me meow")
# fauna = Villager("Fauna", "Deer", "dearie")
# raymond = Villager("Raymond", "Cat", "crisp")
# stitches = Villager("Stitches", "Cub", "stuffin")

# bob.friends = [stitches, raymond, fauna]
# marshal.friends = [raymond, ankha, fauna]

# print(bob.get_mutuals(marshal))

# ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))

# Example Output:

# ['Raymond', 'Fauna']
# []



# Problem 2: Linked Up
# A linked list is a data structure that, similar to a normal list or array, allows us to store pieces of data sequentially. The key difference is how the elements are stored in memory.

# In a normal list, elements are stored in adjacent memory locations. If we know the location of the first element, we can easily access any other element in the list.

# In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Instead, each node stores a reference or pointer to the next node in the list, allowing us to traverse the list.

# Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.

# A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# # Add code here to link the above nodes
# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle
# # Example Usage:

# print_linked_list(kk_slider)
# Example Output:

# K.K. Slider -> Harriet -> Saharah -> Isabelle


# Problem 3: Daily Tasks
# Imagine a linked list used as a daily task list where each node represents a task. Write a function add_task() that takes in the head of a linked list and adds a new node to the front of the task list.

# The function should insert a new Node object with the value task as the new head of the linked list and return the new node.

# Note: The "head" of a linked list is the first element in the linked list. It is equivalent to lst[0] of a normal list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_first(head, task):
    new_node = Node(task) 
    new_node.next = head
    head_A = new_node
    return head_A

# Example Usage:

# task_1 = Node("shake tree")
# task_2 = Node("dig fossils")
# task_3 = Node("catch bugs")
# task_1.next = task_2
# task_2.next = task_3

# # Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))
# Example Output:

# check turnip prices -> shake tree -> dig fossils -> catch bugs



# Problem 4: Halve List
# Write a function halve_list() that accepts the head of a linked list whose values are integers and divides each value by two. Return the head of the modified list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def halve_list(head):
    Current = head
    while Current:
        Current.value = float(Current.value /2)
        Current = Current.next 
    return head

# Example Usage:

# node_one = Node(5)
# node_two = Node(6)
# node_three = Node(7)
# node_one.next = node_two
# node_two.next = node_three

# # Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))

# Example Output:

# 2.5  -> 3 -> 3.5


# Problem 5: Remove Last
# Write a function delete_tail() that accepts the head of a linked list and removes the last node in the list. Return the head of the modified list.

# Note: The "tail" of a list is the last element in the linked list. It is equivalent to lst[-1] in a normal list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_tail(head):
    # check if the list is empty
    if not head:
        return None

    counter = 0
    curr = head
    while curr:
        counter += 1
        curr = curr.next

    index = 1
    curr = head
    while index < counter - 1:
        index += 1
        curr = curr.next
    
    curr.next = None
    return head
    #try now
        # if its not empty 


# Example Usage:

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))

# Example Output:

# Common Butterfly -> Ladybug