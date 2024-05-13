import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


##############################################
# Data Structures and Algorithm Fundamentals #
##############################################


# Lists
# Ordered collection of items, allowing for sequential storange and retrieval
fiction_books = ['Dune', '1984', 'Brave New World', 'Neuromancer']
print(fiction_books)
print(type(fiction_books))


line_break()

# Dictionaries
# key-value pairs, providing a fast and flexible way to retrieve information

book_locations = {
    'Dune': 'Fiction Section, Shelf 2',
    '1984': 'Fiction Section, Shelf 4',
    'Brave New World': 'Fiction Section, Shelf 1',
    'Neuromancer': 'Fiction Section, Shelf 2'
}

print(book_locations)
print(type(book_locations))

line_break()


# Linked List
# Linear Data Structure where each element (node) points to the next one, allowing dynamic and efficient insertion or removal

# Create a Node class for each element that will two attributes:
# .value that will be the value of the node, and then a .next that will point to the next node in the sequence

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<Node|{self.value}>"

    def __str__(self):
        return str(self.value)

# Create a Linked List Class (structure) that has one attribute: .head will point to the first Node in the Linked List
# and a method to print all the values in the Linked List

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        # Start at the head node
        current_node = self.head
        # While the current node is a Node
        while current_node is not None:
            # print the current node
            print(current_node)
            # Set the current node to the next node in the list
            current_node = current_node.next


library_books = LinkedList()
library_books.head = Node('Dune')
library_books.head.next = Node('1984')
library_books.head.next.next = Node('Brave New World')
library_books.head.next.next.next = Node('Neuromancer')

library_books.traverse()

line_break()

# Stacks
# Follow the Last In First Out (LIFO) principle
# think of a stack of pancakes - the most recent pancake made will be the first one eaten.
from collections import deque

browser_history = deque()
browser_history.append("codingtemple.com")
browser_history.append("pythontutor.com")
browser_history.append("w3schools.com")
browser_history.append("docs.python.org")

print(browser_history)

while browser_history:
    current_page = browser_history.pop()
    print('Currently on:', current_page)
    print('Clicking the back button...\n')

print(browser_history)


line_break()

# Queues
# Follow the First In First Out (FIFO) principle
# think of waiting for the hottest tickets in town - the first person in line will be the first person to get tickets

cashier_line = deque()
cashier_line.append('Alice')
cashier_line.append('Bob')
cashier_line.append('Charlie')
cashier_line.append('Danielle')

print(cashier_line)

while cashier_line:
    current_customer = cashier_line.popleft()
    print('Currently ringing up:', current_customer)
    print('Next!\n')

print(cashier_line)

line_break()
# Binary Tree
# Heirerarchical structure where each node has at most two children
# Each node is a Binary Tree itself

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<BinaryTree|{self.value}>"

    def __str__(self):
        return str(self.value)

    def traverse(self):
        print(self)
        if self.left:
            self.left.traverse()
        if self.right:
            self.right.traverse()

root = BinaryTree(50)
root.left = BinaryTree(25)
root.left.left = BinaryTree(10)
root.left.right = BinaryTree(45)
root.right = BinaryTree(75)
root.right.left = BinaryTree(60)
root.right.right = BinaryTree(90)

root.traverse()

line_break()

# Graphs
# consists of nodes and edges, represent relationships between entities

#      Erika
#     /     \
#    /       \
# Felix --- Grace
#    \       /
#     \     /
#      Henry

friend_graph = {
    "Erika": ["Felix", "Grace"],
    "Felix": ["Grace", "Erika", "Henry"],
    "Grace": ["Erika", "Felix", "Henry"],
    "Henry": ["Felix", "Grace"]
}

for person, friends in friend_graph.items():
    print(f"{person} is friends with {', '.join(friends)}")


line_break()
line_break()

#############################
# Data Structure Operations #
#############################

print(fiction_books)

# Sorting Algorithm
# 2 main ways to sort a list - builtin sorted()  and list method .sort
# sorted - out of place - a new sorted list is created from the original
# .sort - in place - the original list is modified

print('Before sorted:', fiction_books)
sorted_books = sorted(fiction_books)
print('After sorted:', fiction_books) # This will still be the same as before the sorted function
print('Sorted return:', sorted_books) # will return the new sorted list

print('Before .sort:', fiction_books)
sorted_books2 = fiction_books.sort()
print('After .sort:', fiction_books) # This will be different as before the .sort method
print('Sort return:', sorted_books2) # will return None, the original list has been modified

# Searching Algorithm
# Searching functions take on the role of detective, looking for specific data
# use the 'in' keyword

# desired_book = input("Please enter a book title: ").title()
desired_book = "1984"
print('Searching...')
if desired_book in fiction_books:
    print(f"{desired_book} is in the Fiction Section")
else:
    print(f"{desired_book} is NOT in the Fiction Section")


# Insertion Algorithm
# Insertion functions add elements while maintaining the structural integrity

print('Inserting...')
new_book = "The Great Gatsby"
fiction_books.append(new_book) # Will add to the end of the list

print(fiction_books)

print("Inserting...")
new_book2 = "The Catcher in the Rye"
fiction_books.insert(2, new_book2) # Will insert at a specific index position
print(fiction_books)


# Deletion Algorithm
# Deletion functions remove elements while maintaining the structural integrity
print("Deleting...")

unwanted_book = 'Neuromancer'
fiction_books.remove(unwanted_book)
print(fiction_books)

fiction_books.pop()
print(fiction_books)

line_break()
line_break()


print('''
You have been tasked with developing a library cataloging system for a local library. The system should allow librarians to efficiently
manage and retrieve books from different sections of the library.

Your task is to implement a Python class called Library that provides the following functionalities:

Adding Books: 
    The add_book method should take two parameters: section (a string indicating the section of the library where the book belongs) and book (a string indicating the title of the book). If the specified section already exists in the library, the book should be added to that section. If the section does not exist, it should be created, and the book should be added to it.

Retrieving Books: 
    The retrieve_books method should take one parameter: section (a string indicating the section of the library from which books should be retrieved). It should return all of the books in the specified section. If the section does not exist or if there are no books in the section, it should return the string "No books available in this section."
''')



class Library:
    def __init__(self):
        self.shelves = {}

    def add_book(self, section, book):
        if section not in self.shelves:
            self.shelves[section] = [book]
        else:
            self.shelves[section].append(book)

    def retrieve_books(self, section):
        return self.shelves.get(section, "No books available in this section.")

# Example usage:
library = Library()

# Adding books to the library
library.add_book("Fiction", "1984")
library.add_book("Fiction", "Brave New World")
library.add_book("Non-Fiction", "Freakonomics")

# Retrieving books from the library
print(library.retrieve_books("Fiction"))  # Output: ["1984", "Brave New World"]
print(library.retrieve_books("Non-Fiction"))  # Output: ["Freakonomics"]
print(library.retrieve_books("Science"))  # Output: "No books available in this section."
