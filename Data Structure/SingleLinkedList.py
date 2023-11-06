class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def Add_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def Add_at_any_index(self, prev_node, new_data):
        if prev_node is not None:
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            print("index cease to exist")    
            return
    def Add_at_the_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
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
        prev.next = temp.next
        temp = None 
    def search(self, x):
        current = self.head
        while current is not None:
            if current.data == x:
                print(f"the element {x} has been found ")
            current = current.next
        print(f"the element {x} doesn't exist in this list")
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
linkedlist1 = LinkedList()
Node1 = Add_at_front("Abo obaidah amk") 
Node2 = Add_at_any_index("Abo obaidah amk",1)
Node3 = Add_at_the_end(3.5)
delete(3.5)
print_list() 

        