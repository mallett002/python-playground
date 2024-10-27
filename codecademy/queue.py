from node import Node

class Queue:
    def __init__(self, limit = 5):
        self.head = None 
        self.tail = None 
        self.size = 0
        self.limit = limit

    def peek(self):
        if self.head:
            return self.head

        return "Nothing in the queue"
    
    def has_space(self):
        return self.size < self.limit

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def enqueue(self, val):
        if not(self.has_space()):
            print('No space left in queue')
            
        else:
            new_node = Node(val)

            if self.is_empty():
                self.head = new_node
                self.tail = new_node

            else: 
                self.tail.set_next_node(new_node)
                self.tail = new_node
            
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print('The queue is currently empty')
            return None

        curr_head = self.head
        next = self.head.get_next_node()
        self.head = next
        self.size -= 1

        return curr_head


def main():
    queue = Queue()
    print('peeking: ', queue.peek())

    queue.enqueue(37)
    print('peeking: ', queue.peek())

    queue.enqueue(38)
    queue.enqueue(39)
    queue.enqueue(40)
    queue.enqueue(41)

    print('peeking: ', queue.peek())
    print('size: ', queue.get_size())

    queue.enqueue(38)

    print('removed from queue: ', queue.dequeue().get_value())
    print('peeking: ', queue.peek().get_value())
    print('size: ', queue.get_size())

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()


if __name__ == '__main__':
    main()
