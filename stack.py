# Simple Stack DataStructure on Python

# Yeah it needs alot of improvement, shut up

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

