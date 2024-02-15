circular queue program:

class CircularQueue:
    def _init_(self, size):
        self.queue = {}
        self.size = size
        self.start = 0
        self.end = 0

    def enqueue(self, element):
        if (self.end - self.start) == self.size:
            self.start += 1
        self.queue[self.end % self.size] = element
        self.end += 1

    def dequeue(self):
        if self.end == self.start:
            raise IndexError("Queue is empty")
        element = self.queue.pop(self.start % self.size)
        self.start += 1
        return element

def main_circular_queue():
    """
    The main function to demonstrate the usage of CircularQueue.
    """
    cq = CircularQueue(5)
    for i in range(7):
        cq.enqueue(i)
        print(f"Enqueued: {i}")

    print("Queue:", cq.queue)
    for i in range(3):
        print(f"Dequeued: {cq.dequeue()}")

    print("Queue after dequeue operations:", cq.queue)

# Example usage:
main_circular_queue()