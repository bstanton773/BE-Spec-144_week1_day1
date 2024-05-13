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


#############################
# Time and Space Complexity #
#############################

# Big O notation is a mathematical notation used in computer science to describe the performance or complexity of an 
# algorithm. It provides a way to express the upper bound of the time or space required by an algorithm as a function 
# of the size of the input.

# Time complexity refers to the amount of time an algorithm takes to complete as a function of the size of its input. 
# It's typically expressed using Big O notation and describes how the runtime of an algorithm grows as the input size increases.

# Space complexity, on the other hand, refers to the amount of memory space an algorithm requires as a function 
# of the size of its input. Like time complexity, it's also expressed using Big O notation and describes how the 
# memory usage of an algorithm grows as the input size increases.

# Understanding time and space complexity helps developers analyze and compare different algorithms to determine which 
# ones are more efficient for solving specific problems. It's a crucial concept in algorithm design and optimization.

# Complexities - Best to Worst
# O(1) - Constant
# O(log n) - logarithmic
# O(n) - linear
# O(n log n) - linear logarithmic
# O(n**2) - quadratic

# Analyzing a Best, Worst, and Average Case by measuring code efficiency

contacts = [
    ("Alice", "555-1234"),
    ("Bob", "555-5678"),
    ("Charlie", "555-9012"),
    ("David", "555-3456"),
    ("Emma", "555-7890"),
    ("Frank", "555-2345"),
    ("Grace", "555-6789"),
    ("Henry", "555-0123"),
    ("Ivy", "555-4567"),
    ("Jack", "555-8901"),
    ("Kate", "555-3456"),
    ("Liam", "555-7890"),
    ("Mia", "555-2345"),
    ("Noah", "555-6789"),
    ("Olivia", "555-0123"),
    ("Peter", "555-4567"),
    ("Quinn", "555-8901"),
    ("Rachel", "555-2345"),
    ("Sam", "555-6789"),
    ("Taylor", "555-0123"),
    ("Uma", "555-4567"),
    ("Victor", "555-8901"),
    ("Wendy", "555-2345"),
    ("Xavier", "555-6789"),
    ("Yara", "555-0123"),
    ("Zoe", "555-4567")
]

def get_phone_number(address_book, target_name):
    # Loop through each tuple in the address book
    for person, number in address_book:
        # Compare the person with the target name
        if person == target_name:
            # Return the number associated
            return number
    # If we loop through all of the contacts, we know that the target name is not in it
    return -1

# Best Case - O(1) - Contant Time
print(get_phone_number(contacts, 'Alice'))

# Worst Case - O(n) - Linear Time
print(get_phone_number(contacts, 'Zoe'))

# Average Case - O(n) - (technically O(n/2) => O(n))
print(get_phone_number(contacts, 'Mia'))

line_break()
# Time and Space Complexities
fruits = ["apple", "banana", "orange", "grape", "kiwi", "mango", "strawberry"]

# Indexing a list
# Constant Time and Space - O(1)
indexing = fruits[-1]
print(indexing)

# Searching through a list
# Linear Time - O(n) and Constant Space - O(1)
print('mango' in fruits)
print('blueberry' in fruits)

# Copying a List
# Linear Time - O(n) and Linear Space - O(n)
copied_fruits = fruits[:]
print(copied_fruits)

# Assigning a list index a value
# Constant Time - O(1) and Constant Space - O(1)
fruits[3] = 'grapefruit'
print(fruits)


# Insertion - list.append
# Constant Time - O(1) and Constant Space - O(1)
fruits.append('watermelon')
print(fruits)

# Insertion - list.insert
# Linear Time - O(n) and Constant Space - O(1)
fruits.insert(0, 'pear')
print(fruits)


# Deletion - list.pop - default -1
# Constant Time - O(1) and Constant Space - O(1)
last_element = fruits.pop()
print(fruits)
print(last_element)

# list.pop - anything other than -1
# Linear Time - O(n) and Constant Space - O(1)
first_element = fruits.pop(0)
print(fruits)
print(first_element)


# Sorting - Python list uses timsort
# Linear Logarithmic - O(n log n) and Constant Space - O(1)
fruits.sort()
print(fruits)


line_break()
# Time and Space Complexities of Python Dictionaries

fruit_counts = {}

# Insertion
# Constant Time and Constant Space - O(1)
fruit_counts['apple'] = 10
fruit_counts['banana'] = 15
fruit_counts['orange'] = 20

print(fruit_counts)

# Accessing
# Constant Time and Constant Space - O(1)
print(fruit_counts['apple'])
print(fruit_counts.get('banana'))
print(fruit_counts.get('strawberry', 'No strawberries'))

# Searching
# Constant Time and Constant Space - O(1)
print('orange' in fruit_counts)

# Updating values via key
# Constant Time and Constant Space - O(1)
fruit_counts['banana'] = 30
print(fruit_counts)

# Removing key,value pairs
# Constant Time and Constant Space - O(1)
del fruit_counts['apple']
fruit_counts.pop('orange')
print(fruit_counts)

# Real World Applications

# users = [
#     ["user1", "password1"], 
#     ["user2", "password2"], 
#     ["user3", "password3"]
# ]

# username = input("Enter username: ")
# password = input("Enter password: ")

# for user in users:
#     if user[0] == username and user[1] == password:
#         print('You have logged in')
#         break
# else:
#     print('Incorrect username and/or password')


# Ex. 1 Storing User Credentials
# # Set up dictionary to hold users
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Verifiy a user
# Ask for username and password and check that against the dictionary

# username = input("Enter username: ")
# password = input("Enter password: ")
username = "user2"
password = "password2"

if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid username or password")


# Ex. 2 - Inventory Management

inventory = {
    'orange': 100,
    'banana': 75,
    'apple': 150
}

# Update the inventory
inventory['orange'] -= 20 # Sold 20 oranges
inventory['apple'] += 25 # Recevied 25 apple shipment

print(inventory)

line_break()
line_break()

print('''
You are tasked with developing a contact management system to help users organize their contacts. The system should allow users to add 
new contacts, view existing contacts, search for contacts by name, and delete contacts.

1. Create an empty list named **`contacts`** to store contact information.
2. Implement a function named **`add_contact`** that takes a name, phone number, and email address as input and adds them to the **`contacts`** list as a dictionary.
3. Implement a function named **`view_contacts`** that displays all contacts in the **`contacts`** list along with their details.
4. Implement a function named **`search_contact`** that takes a name as input and searches for the contact in the **`contacts`** list. If found, display the contact details; otherwise, print a message indicating that the contact was not found.
5. Implement a function named **`delete_contact`** that takes a name as input and removes the contact from the **`contacts`** list if it exists.
6. Test your implementation by adding contacts, viewing them, searching for contacts, and deleting contacts.
''')


# Step 1: Create an empty list to store contacts
contacts = []

# Step 2: Add contact to the contacts list
def add_contact(name, phone, email):
    contact = {'Name': name, 'Phone': phone, 'Email': email}
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

# Step 3: View all contacts
def view_contacts():
    print("Contacts:")
    for contact in contacts:
        print(f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\n")
    print(f"Viewing contacts completed.")

# Step 4: Search for a contact by name
def search_contact(name):
    found = False
    for contact in contacts:
        if contact['Name'] == name:
            print("Contact Found:")
            print(f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\n")

            found = True
            break
    if not found:
        print("Contact not found.")
    print(f"Searching contact completed.")

# Step 5: Delete a contact by name
def delete_contact(name):
    for contact in contacts:
        if contact['Name'] == name:
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            print(f"Deleting contact completed.")
            return
    print("Contact not found.")

# Test the implementation
add_contact('John Doe', '123-456-7890', 'john@example.com')
add_contact('Jane Smith', '987-654-3210', 'jane@example.com')
view_contacts()

search_contact('John Doe')
search_contact('Alice')
delete_contact('Jane Smith')

view_contacts()
