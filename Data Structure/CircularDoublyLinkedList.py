class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None 

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def Add_at_front(self, new_data):
        new_node = Node(new_data)
        #cur = self.head
        #new_node.next = self.head
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
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
            new_node.next = self.head
            self.head.prev = new_node
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
            new_node.next = self.head
            self.head.prev = new_node
            return
        else:
            last = self.head
            while(last.next != self.head):
                last = last.next
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node
        
    def delete(self, key):
        cur = self.head
        if cur is not None:
            if cur.data == key:
                cur.next = self.head
                cur = None
        while (cur is not None):
            if cur.data == key:
                break
            prev = cur 
            cur = cur.next
        if cur == None:
            return
        else:
            prev.next = cur.next
            cur = None 
        
    def search(self, x):
        cur = self.head
        while cur is not None:
            if cur.data == x:
                print(f"the element \"{x}\" has been found ")
                break
            cur = cur.next
        else:
            print(f"the element \"{x}\" doesn't exist in this list")
            
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head: #exits the loop when it reaches to the end
                break

        