class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  


class LinkedList:
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

    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

   
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    
    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data: 
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        if current_node.next is None:
            print(f"Node with data {data} not found")
        else:
            current_node.next = current_node.next.next


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.prepend(0)
llist.display()  
llist.delete(2)
llist.display()  
