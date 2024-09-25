class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node with the given key
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    # Check if the tree contains a given key
    def contains(self, key):
        return self._contains(self.root, key)

    def _contains(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._contains(node.left, key)
        else:
            return self._contains(node.right, key)

    # Delete a node with the given key
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._minValueNode(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # In-order Traversal: Left -> Root -> Right
    def inorder_traversal(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)

    # Pre-order Traversal: Root -> Left -> Right
    def preorder_traversal(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.key, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)

    # Post-order Traversal: Left -> Right -> Root
    def postorder_traversal(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=' ')

    # Find the closest value to a given target in the BST
    def find_closest(self, target):
        return self._find_closest(self.root, target, float('inf'))

    def _find_closest(self, node, target, closest):
        if node is None:
            return closest
        if abs(target - closest) > abs(target - node.key):
            closest = node.key
        if target < node.key:
            return self._find_closest(node.left, target, closest)
        elif target > node.key:
            return self._find_closest(node.right, target, closest)
        else:
            return closest

    # Validate if the tree is a BST
    def is_valid_bst(self):
        return self._is_valid_bst(self.root, float('-inf'), float('inf'))

    def _is_valid_bst(self, node, min_value, max_value):
        if node is None:
            return True
        if not (min_value < node.key < max_value):
            return False
        return (self._is_valid_bst(node.left, min_value, node.key) and
                self._is_valid_bst(node.right, node.key, max_value))

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Inserting elements
    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)
    
    print("In-order Traversal:")
    bst.inorder_traversal()  # Output: 20 30 40 50 60 70 80

    print("Pre-order Traversal:")
    bst.preorder_traversal()  # Output: 50 30 20 40 70 60 80

    print("Post-order Traversal:")
    bst.postorder_traversal()  # Output: 20 40 30 60 80 70 50

    # Check if tree contains an element
    print("Contains 40:", bst.contains(40))  # Output: True
    print("Contains 100:", bst.contains(100))  # Output: False

    # Deleting an element
    bst.delete(70)
    print("In-order Traversal after deleting 70:")
    bst.inorder_traversal()  # Output: 20 30 40 50 60 80

    # Find closest value
    print("Closest value to 65:", bst.find_closest(65))  # Output: 60

    # Validate if tree is a BST
    print("Is the tree a valid BST?", bst.is_valid_bst())  # Output: True
