class Node:
    def __init__(self, data):
        # Node class for a doubly linked list
        self.data = data
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        # Doubly linked list class with head pointer
        self.head = None

    def Add_at_front(self, new_data):
        # Function to add a new node at the front of the doubly linked list
        new_node = Node(new_data)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        else:
            # If the list is not empty, update pointers to add the new node at the front
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def Add_at_any_index(self, prev_node, new_data):
        # Function to add a new node after a specific node in the doubly linked list
        if prev_node is None:
            # If the specified previous node does not exist, print an error message
            print("Index does not exist")
            return
        new_node = Node(new_data)
        if prev_node.next is None:  # If prev_node is the last node
            # If prev_node is the last node, update pointers to add the new node at the end
            prev_node.next = new_node
            new_node.prev = prev_node
        else:
            # If prev_node is not the last node, update pointers accordingly to insert the new node
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            if new_node.next is not None:
                new_node.next.prev = new_node
        
            
    def Add_at_the_end(self, new_data):
        # Function to add a new node at the end of the doubly linked list
        new_node = Node(new_data)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        else:
            # If the list is not empty, traverse to the last node and update pointers to add the new node at the end
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
        
    def delete(self, key):
        # Function to delete a node with a specific value from the doubly linked list
        cur = self.head
        if cur is not None:
            if cur.data == key:
                if cur.next == self.head:  # If there is only one node
                    self.head = None
                    return
                else:
                    last = self.head.prev  # Get the last node
                    self.head = self.head.next  # Update the head to the next node
                    last.next = self.head  # Update the last node's next pointer to the new head
                    self.head.prev = last  # Update the head's prev pointer to the last node
                    cur = None
                    return

        while cur is not None:
            if cur.data == key:
                break
            prev = cur
            cur = cur.next

        if cur is None:
            return
        # Update pointers to delete the node with the specified key
        prev.next = cur.next
        cur.next.prev = prev
        
    def search(self, x):
        # Function to search for a specific value in the doubly linked list
        current = self.head
        while current is not None:
            if current.data == x:
                # If the element is found, print a message
                print(f"The element \"{x}\" has been found ")
                break
            current = current.next
        else:
            # If the element is not found, print a message
            print(f"The element \"{x}\" doesn't exist in this list")
            
    def print_list(self):
        # Function to print the doubly linked list
        temp = self.head
        while temp:
            # Traverse through the list and print each node's data
            print(temp.data)
            temp = temp.next
