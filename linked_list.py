# O v o

# Node Object
class Node(object):
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

# A Linked List thing
class LinkedList:
    def __init__(self):
        self.Head = Node()
        self.size = 0

    def append(self, value):
        if self.Head.value == None:
            self.Head.value = value
            self.size += 1
            return
        this = self.Head
        while this.next_node != None:
            this = this.next_node
        self.size += 1
        this.next_node = Node(value)

    def append_last(self, value):
        this = self.Head
        while this != None and this.next_node != None:
            this = this.next_node
        self.size += 1
        this.next_node = Node(value)

    def append_at(self, value, index):
        this = self.Head
        if index == 0:
            self.append(value)
        elif index == self.size:
            self.append_last(value)
        elif index > self.size:
            raise Exception("ERROR: index larger than Linked List size Throw something smaller jackass!")
        else:
            counter = 0
            while this.next_node != None:
                if counter == index - 1:
                    temp = this.next_node
                    this.next_node = Node(value)
                    this.next_node.next_node = temp
                    break
                this = this.next_node
                counter += 1
            
    def remove(self, index=None):
        this = self.Head
        if index > self.size:
            raise Exception("ERROR: index larger than Linked List size Throw something smaller jackass!")

        if index == None:
            this.value = None
        else:
            counter = 1
            while this != None:
                if counter == index:
                    this.value = None
                    break
                counter += 1
                this = this.next_node

    def clear(self):
        self.Head = None
        self.size = 0

    def exists(self, target_value):
        this = self.Head
        while this != None:
            if this.value == target_value:
                return True
            this = this.next_node
        return False

    def get_value(self, index):
        this = self.Head
        if index > self.size:
            raise Exception("ERROR: index larger than Linked List size Throw something smaller jackass!")
        counter = 0
        while this != None:
            if counter == index:
                return this.value
            counter += 1
            this = this.next_node

    def print_list(self):
        this = self.Head
        while this != None:
            print(this.value)
            this = this.next_node
