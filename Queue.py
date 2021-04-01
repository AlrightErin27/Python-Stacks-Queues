class Queue:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        """Returns True if Queue is empty, False otherwise"""
        if len(self.data) == 0:
          return True
        else:
          return False
    def enqueue(self, item):
        """Adds an item to the back of queue"""
        self.data.append(item)
    def dequeue(self):
        """Removes the item from the front of queue. Returns the removed item"""
        popped_item = self.data.pop(0)
        return popped_item
    def peek(self):
        """Returns the first item in the queue, but doesn't remove it"""
        return self.data[0]
    def size(self):
        """Returns the (int) size of the queue"""
        return len(self.data)
    def __str__(self):
        """Returns a string representation of all items in queue"""
        data_string = ' '.join(self.data)
        return f'{data_string}'
### TEST SUITE ###
# Use the following code to help you implement the Queue
my_queue = Queue()
print('Is Queue empty?', my_queue.isEmpty())
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
my_queue.enqueue('D')
print('Dequeued item:', my_queue.dequeue())
print('First item:', my_queue.peek())
print('Here are all the items in the queue:', my_queue)
print('The size of my stack is:', my_queue.size())