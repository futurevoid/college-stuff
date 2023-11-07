class Node:
    def __init__(self, data):
        # Node class for creating nodes of the linked list
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Constructor to initialize the linked list
        self.head = None

    def Add_at_front(self, new_data):
        # Function to add a new node at the front of the linked list
        new_node = Node(new_data)
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        else:  # If the list is not empty, set the new node as the head and update pointers
            new_node.next = self.head
            self.head = new_node

    def Add_at_any_index(self, prev_node, new_data):
        # Function to add a new node after a specific node in the linked list
        if prev_node is None:  # Check if the previous node exists
            print("Index does not exist")
            return
        new_node = Node(new_data)
        if prev_node.next is None:  # If prev_node is the last node, set the next of prev_node to the new_node
            prev_node.next = new_node
        else:  # If prev_node is not the last node, update pointers accordingly
            new_node.next = prev_node.next
            prev_node.next = new_node

    def Add_at_the_end(self, new_data):
        # Function to add a new node at the end of the linked list
        new_node = Node(new_data)
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
            return
        last = self.head
        while(last.next):  # Traverse the list to find the last node
            last = last.next
        last.next = new_node  # Set the next of the last node to the new_node

    def delete(self, key):
        # Function to delete a node with a specific value from the linked list
        temp = self.head
        if temp is not None:
            if temp.data == key:  # If the head node contains the key, update the head and delete the previous head
                self.head = temp.next
                temp = None
        while (temp is not None):
            if temp.data == key:  # Find the node with the key and delete it
                break
            prev = temp
            temp = temp.next
        if temp is None:  # If the key is not found, return
            return
        prev.next = temp.next  # Update pointers to remove the node with the key
        temp = None

    def search(self, x):
        # Function to search for a specific value in the linked list
        current = self.head
        while current is not None:  # Traverse the list and search for the element
            if current.data == x:
                print(f"the element \"{x}\" has been found ")
                break
            current = current.next
        else:  # If the element is not found, print a message
            print(f"the element \"{x}\" doesn't exist in this list")

    def print_list(self):
        # Function to print the linked list
        temp = self.head
        while temp:  # Traverse the list and print each node's data
            print(temp.data)
            temp = temp.next
