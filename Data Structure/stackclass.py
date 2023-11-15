class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        if self.items == []:
            print("The stack is empty")

        else:
            print("The stack is not empty")

    def push(self, item):
        self.items.append(item)

    def pop(self, index=...):
        if index == ...:
            return self.items.pop()
        else:
            return self.items.pop(index)

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def printstack(self):
        if self.items == []:
            return
        elements = self.peek()

        self.pop()
        self.printstack()

        print(elements)

        self.push(elements)
