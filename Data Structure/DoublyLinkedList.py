class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def Add_at_front(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def Add_at_any_index(self, prev_node, new_data):
        if prev_node is None:
            print("Index does not exist")
            return
        new_node = Node(new_data)
        if prev_node.next is None:  # If prev_node is the last node
            prev_node.next = new_node
            new_node.prev = prev_node
        else:
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            if new_node.next is not None:
                new_node.next.prev = new_node
        
            
    def Add_at_the_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = new_node
            new_node.prev = last
        
    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                temp.next = self.head
                temp = None
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp 
            temp = temp.next
        if temp == None:
            return
        else:
            prev.next = temp.next
            temp = None 
        
    def search(self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                print(f"the element \"{x}\" has been found ")
                break
            current = current.next
        else:
            print(f"the element \"{x}\" doesn't exist in this list")
            
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    

        