# class Stack:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#     def push(self,name):
#         k = name.split()
#         i = 0
#         while i<len(k):
#             self.s1.append(k[i])
            
#             i = i + 1
        
#         while self.s1:
#             self.s2.append(self.s1.pop())
#         return ' '.join(self.s2)
# s = Stack()
# print(s.push('nihala shirin'))


# class Stack:
#     def __init__(self):
#         self.s2 = []
    
#     def push(self,lst):
#         while lst:
#             self.s2.append(lst.pop())
#             lst[:-1]
        

# lst = ['apple','orange','graped']
# s = Stack()
# s.push(lst)
# print(s.s2)
