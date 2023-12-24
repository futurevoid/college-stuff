class Node:
    def __init__(self, data):
        # Node class for creating nodes of the linked list
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Constructor to initialize the linked list
        self.head = None

    def Prepend(self, new_data):
        # Function to add a new node at the front of the linked list
        new_node = Node(new_data)
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        else:  # If the list is not empty, set the new node as the head and update pointers
            new_node.next = self.head
            self.head = new_node

    def Insert(self, index, new_data):
        if index == 0:
            self.Prepend(new_data)
            return
        newnode = Node(new_data)
        current = self.head
        for i in range(index - 1):
            current = current.next
            if not current:
                print("invalid or non-existent index")
                return
        if current.next is None:
            current.next = newnode
            return
        else:
            newnode.next = current.next
            current.next = newnode

    def Append(self, new_data):
        # Function to add a new node at the end of the linked list
        new_node = Node(new_data)
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse the list to find the last node
            last = last.next
        last.next = new_node  # Set the next of the last node to the new_node

    def delete(self, key):
        # Function to delete a node with a specific value from the linked list
        current = self.head
        if current is not None:
            if (
                current.data == key
            ):  # If the head node contains the key, update the head and delete the previous head
                self.head = current.next
                current = None
        while current is not None:
            if current.data == key:  # Find the node with the key and delete it
                break
            prev = current
            current = current.next
        if current is None:  # If the key is not found, return
            return
        prev.next = current.next
        current = None

    def search(self, x):
        # Function to search for a specific value in the linked list
        current = self.head
        while current is not None:  # Traverse the list and search for the element
            if current.data == x:
                print(f'the element "{x}" has been found ')
                break
            current = current.next
        else:  # If the element is not found, print a message
            print(f'the element "{x}" doesn\'t exist in this list')

    def print_list(self):
        # Function to print the linked list
        current = self.head
        while current:  # Traverse the list and print each node's data
            print(current.data)
            current = current.next
