# A Queue implementation using Stacks on Python
# By the way I'm doing this to prepare my body to DS
# Yeah by the time I wrote this I haven't took DS nor anything like that and also yeah kinda should make a "My Cpp Projects" Folder for a Cpp version anyway why I'm still writting this while also thinking about it also I think there's a typo here why I'm still writing? Anyway enjoy

class Node(object):
    def __init__(self, value:object=None, next_node=None):
        self.value = value
        self.next_node = next_node
        
        
class Stack:
    def __init__(self):
        self.head = Node()
        self.size: int = 0

    def push(self, value: object):
        this = self.head
        self.head = Node(value)
        self.head.next_node = this
        self.size += 1

    def pop(self) -> object:
        this = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        return this

    def is_empty(self):
        return self.size == 0

    def search(self, item: object) -> int:
        this = self.head
        counter = 0
        if this != None:
            counter += 1
        while this.next_node != None:
            if item == this.value:
                break
            counter += 1
            this = this.next_node
        return counter

    def peek(self) -> object:
        this = self.head
        if this != None:
            return this.value


class Queue:
    def __init__(self):
        self.In = Stack()
        self.Out = Stack()

    def add(self, item: object) -> object:
        self.In.push(item)

    def peek(self):

        if self.Out.is_empty():
            while not self.In.is_empty():
                self.Out.push(self.In.pop())
            
        return self.Out.peek()

    def poll(self) -> object:
        if self.Out.is_empty():
            while not self.In.is_empty():
                self.Out.push(self.In.pop())
            
        return self.Out.pop()

    def is_empty(self) -> bool:
        return self.In.size + self.Out.size == 0
