class Queue:
    def __init__(self, initValues: list = None):
        self.queue = []
        self.size = 0

        if initValues is not None:
            self.queue = initValues

    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def isEmpty(self) -> bool:
        return self.size == 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(self.queue)