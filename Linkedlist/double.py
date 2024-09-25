class Node:
    def __init__(self, data):
        self.data = data     
        self.next = None     
        self.prev = None      


class DoublyLinkedList:
    def __init__(self):
        self.head = None  

   
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:  
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node


    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:  
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def display_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

  
    def display_backward(self):
        last_node = self.head
        while last_node and last_node.next:
            last_node = last_node.next  

        while last_node:
            print(last_node.data, end=" -> ")
            last_node = last_node.prev
        print("None")

    def delete(self, data):
        if self.head is None: 
            print("List is empty")
            return

        current_node = self.head

        
        if current_node.data == data:
            if current_node.next: 
                current_node.next.prev = None
            self.head = current_node.next
            return

        while current_node and current_node.data != data:
            current_node = current_node.next

        if current_node is None:
            print(f"Node with data {data} not found")
        else:
            if current_node.next:
                current_node.next.prev = current_node.prev
            if current_node.prev:
                current_node.prev.next = current_node.next

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.prepend(0)
dllist.display_forward()  
dllist.display_backward()  
dllist.delete(2)
dllist.display_forward() 
