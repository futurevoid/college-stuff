class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        # Initialize an empty circular linked list with no head node
        self.head = None

    def Add_at_front(self, new_data):
        # Function to add a new node at the front of the circular linked list
        new_node = Node(new_data)
        cur = self.head
        new_node.next = self.head
        if self.head is None:
            # If the list is empty, set the new node as the head and make it circular
            new_node.next = new_node
        else:
            # If the list is not empty, traverse to the last node and update pointers to make it circular
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
        self.head = new_node

    def Add_at_any_index(self, prev_node, new_data):
        # Function to add a new node after a specific node in the circular linked list
        if prev_node is None:
            # If the previous node does not exist, print an error message
            print("Index does not exist")
            return
        new_node = Node(new_data)
        if prev_node.next is self.head:  
            # If prev_node is the last node, set the next of prev_node to the new_node
            prev_node.next = new_node
        else:
            # If prev_node is not the last node, update pointers accordingly
            new_node.next = prev_node.next
            prev_node.next = new_node

    def Add_at_the_end(self, new_data):
        # Function to add a new node at the end of the circular linked list
        new_node = Node(new_data)
        if self.head is None: 
            # If the list is empty, set the new node as the head and make it circular
            self.head = Node(new_data)
            self.head.next = self.head
        else:
            # If the list is not empty, traverse to the last node and update pointers to make it circular
            new_node = Node(new_data)
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            new_node.next = self.head

    def delete(self, key):
        if self.head is None:
            return
    
        cur = self.head
        if cur.data == key:  # If the head node contains the key
            if cur.next == self.head:  # If there is only one node
                self.head = None
                return
            else:
                last = self.head.prev  # Get the last node
                self.head = self.head.next  # Update the head to the next node
                last.next = self.head  # Update the last node's next pointer to the new head
                self.head.prev = last  # Update the head's prev pointer to the last node
                return
    
        prev = None
        while cur.next != self.head:
            if cur.data == key:
                break
            prev = cur
            cur = cur.next
    
        if cur.next == self.head:  # If the last node contains the key
            prev.next = self.head
            self.head.prev = prev
            return
    
        prev.next = cur.next
        cur.next.prev = prev


    def search(self, x):
        # Function to search for a specific value in the circular linked list
        cur = self.head
        if cur is not None:
            while cur.next is not self.head:
                if cur.data == x:
                    print(f"the element \"{x}\" has been found ")
                    break
                cur = cur.next
        else:        
            print(f"the element \"{x}\" doesn't exist in this list")

    def print_list(self):
        # Function to print the circular linked list
        cur = self.head
        while cur:  # Traverse the list and print each node's data
            print(cur.data)
            cur = cur.next
            if cur == self.head: #exits the loop when it reaches to the end
                break
