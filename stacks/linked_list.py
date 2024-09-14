# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.nref = None

# class linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def add(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#         n = self.head
#         while n.nref is not None:
#             n = n.nref
#         n.nref = new_node
        
#     def pop(self):
#         if self.head is None:
#             return
#         if self.head.nref is None:
#             self.head = None
#             return
#         n = self.head
#         while n.nref.nref is not None:
#             n = n.nref
#         n.nref = n.nref.nref
        
#     def print_ll(self):
#         n = self.head
#         while n is not None:
#             print(n.data,end=' ---> ')
#             n = n.nref
#         print('None')
        
# l = linkedlist()
# l.add(1)
# l.add(2)
# l.add(3)
# l.add(4)
# l.pop()
# l.print_ll()



# class Node:
#     def __init__(self,data) :
#         self.data = data
#         self.nref = None
#         self.pref = None

# class doublylinkedlist:
#     def __init__(self) :
#         self.head = None
        
#     def push(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
        
#         n = self.head
#         while n.nref is not None:
#             n = n.nref
            
#         n.nref = new_node
#         new_node.pref = n
#         self.tail = new_node
        
        
#     def pop(self):
        
#         if self.head.nref is None:
#             self.head = None
#             return
#         self.tail = self.tail.pref
#         self.tail.nref = None
        
        
        
#     def print_ll(self):
#         n = self.head
#         while n is not None:
#             print(n.data,end=" ---> ")
#             n = n.nref
#         print('None')
        
#     def print_reverse(self):
#         n = self.tail
#         while n is not None:
#             print(n.data,end=' ---> ')
#             n = n.pref
#         print('None')
        
        
# d = doublylinkedlist()
# d.push(1)
# d.push(2)
# d.push(3)
# d.push(5)
# d.push(6)
# d.pop()
# d.pop()

# d.print_ll()
# d.print_reverse()