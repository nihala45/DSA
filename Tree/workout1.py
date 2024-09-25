# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         self.root = self._insert(self.root, key)

#     def _insert(self, root, key):
#         if root is None:
#             return Node(key)
#         elif key < root.key:
#             root.left = self._insert(root.left, key)
#         else:
#             root.right = self._insert(root.right, key)
#         return root

#     def search(self, key):
#         return self._search(self.root, key)

#     def _search(self, root, key):
#         if root is None or root.key == key:
#             return root
#         elif key < root.key:
#             return self._search(root.left, key)
#         else:
#             return self._search(root.right, key)

#     def delete(self, key):
#         self.root = self._delete(self.root, key)

#     def _delete(self, root, key):
#         if root is None:
#             return root
#         if key < root.key:
#             root.left = self._delete(root.left, key)
#         elif key > root.key:
#             root.right = self._delete(root.right, key)
#         else:
#             if root.left is None:
#                 return root.right
#             elif root.right is None:
#                 return root.left
#             temp = self._minValueNode(root.right)
#             root.key = temp.key
#             root.right = self._delete(root.right, temp.key)
#         return root

#     def _minValueNode(self, node):
#         current = node
#         while current.left is not None:
#             current = current.left
#         return current

#     def inorder(self):
#         self._inorder(self.root)

#     def _inorder(self, root):
#         if root is not None:
#             self._inorder(root.left)
#             print(root.key, end=' ')
#             self._inorder(root.right)

# # Example usage:
# bst = BST()
# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# bst.insert(20)
# bst.insert(40)
# bst.insert(60)
# bst.insert(80)
# bst.inorder() 
# print()
# print(bst.search(40) is not None)  
# bst.delete(70)
# bst.inorder()  



class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')

# Example usage:
tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("In-order Traversal:")
tree.inorder(tree.root)  # Output: 4 2 5 1 3
print("\nPre-order Traversal:")
tree.preorder(tree.root)  # Output: 1 2 4 5 3
print("\nPost-order Traversal:")
tree.postorder(tree.root)  # Output: 4 5 2 3 1
