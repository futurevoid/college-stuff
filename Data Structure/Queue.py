class Queue:
    def init(self):
        self.queue = []

    # Add an element

    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display the queue

    def PrintQueue(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
