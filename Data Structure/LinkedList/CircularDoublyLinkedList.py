class Node:
    def __init__(self, data):
        # Node class for creating nodes of the circular doubly linked list
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        # Constructor to initialize the circular doubly linked list
        self.head = None
        
    def Add_at_front(self, new_data):
        # Function to add a new node at the front of the circular doubly linked list
        new_node = Node(new_data)
        if self.head is None:
            # If the list is empty, set the new node as the head and make it circular
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # If the list is not empty, update pointers accordingly to add the node at the front
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
        self.head = new_node
        
    def Add_at_any_index(self, prev_node, new_data):
        # Function to add a new node after a specific node in the circular doubly linked list
        if prev_node is None:
            # Check if the previous node exists
            print("Index does not exist")
            return
        new_node = Node(new_data)
        if prev_node.next is None:
            # If prev_node is the last node
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = self.head
            self.head.prev = new_node
        else:
            # If prev_node is not the last node, update pointers accordingly
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            if new_node.next is not None:
                new_node.next.prev = new_node
        
    
                
    def Add_at_the_end(self, new_data):
        # Function to add a new node at the end of the circular doubly linked list
        new_node = Node(new_data)
        if self.head is None:
            # If the list is empty, set the new node as the head and make it circular
            self.head = new_node
            new_node.next = self.head
            self.head.prev = new_node
            return
        else:
            # If the list is not empty, update pointers accordingly to add the node at the end
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node
        
    def delete(self, key):
        # Function to delete a node with a specific value from the circular doubly linked list
        cur = self.head
        if cur is not None:
            if cur.data == key:
                # If the head node contains the key, update the head and delete the previous head
                cur.next = self.head
                cur = None
        while (cur is not None):
            if cur.data == key:
                break
            prev = cur 
            cur = cur.next
        if cur == None:
            # If the key is not found, return
            return
        else:
            # Update pointers to remove the node with the key
            prev.next = cur.next
            cur = None 
        
    def search(self, x):
        # Function to search for a specific value in the circular doubly linked list
        cur = self.head
        while cur is not None:
            # Traverse the list and search for the element
            if cur.data == x:
                print(f"the element \"{x}\" has been found ")
                break
            cur = cur.next
        else:
            # If the element is not found, print a message
            print(f"the element \"{x}\" doesn't exist in this list")
            
    def print_list(self):
        # Function to print the circular doubly linked list
        cur = self.head
        while cur:
            # Traverse the list and print each node's data
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                # Exit the loop when it reaches the end
                break
