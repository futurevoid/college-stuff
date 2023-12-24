from hmac import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def Prepend(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def Append(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, index, new_data):
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

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


SLL = SingleLinkedList()

SLL.Prepend(8)
SLL.Append(16)
SLL.Append(16)
SLL.insert(2, 12)
SLL.print()
