class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def Addatfront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def Add_at_any_index(self, prev_node, new_data):
        if prev_node != None:
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            print("index cease to exist")    
            return