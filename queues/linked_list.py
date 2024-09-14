class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def enequeue(self,data):
        new_node = Node(data)
        while self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.nref = new_node
        new_node.pref = self.tail
        self.tail = new_node
        
    def dequeue(self):
        if self.head is None:
            return
        self.head = self.head.nref
        self.head.pref = None
    
    def print_ll(self):
        n = self.head
        while n is not None:
            print(n.data, end=' ---> ')
            n = n.nref
        print('None')
    def print_reverse(self):
        n = self.tail
        while n is not None:
            print(n.data,end=' ---> ')
            n = n.pref
        print('None')
    
l = linkedlist()
l.enequeue(1)
l.enequeue(2)
l.enequeue(3)
l.enequeue(4)
l.enequeue(5)
l.dequeue()
# l.dequeue()

l.print_ll()
l.print_reverse()