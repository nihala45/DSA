class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
class CircularLinkedList:
    def __init__(self):
        self.head = None  

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head 
        else:
            temp = self.head
            while temp.next != self.head:  
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head 

  
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = new_node
            new_node.next = self.head  
        else:
            temp = self.head
            while temp.next != self.head:  
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node


    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

 
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            if self.head.next == self.head:  
                self.head = None
            else:
                last = self.head
                while last.next != self.head:  
                    last = last.next
                last.next = self.head.next
                self.head = self.head.next
            return

   
        prev = None
        current = self.head
        while current.next != self.head:
            if current.data == data:
                break
            prev = current
            current = current.next

        if current.data != data:
            print(f"Node with data {data} not found")
        else:
            prev.next = current.next


cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.prepend(0)
cllist.display()  
cllist.delete(2)
cllist.display()  
