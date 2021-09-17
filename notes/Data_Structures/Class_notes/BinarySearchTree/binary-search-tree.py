class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._insert(value, node.left)
            else:
                node.left = TreeNode(value)
        else:
            if node.right is not None:
                self._insert(value, node.right)
            else:
                node.right = TreeNode(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if value == node.value:
            return node
        elif (value < node.value and node.left is not None):
            return self._find(value, node.left)
        elif (value > node.value and node.right is not None):
            return self._find(value, node.right)

    def delete_tree(self):
        # garbage collector will do this for us.
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + ' ')
            self._print_tree(node.right)

#     3
# 0     4
#   2      8


# Example 1
tree1 = BST()
tree1.insert(10)
tree1.insert(5)
tree1.insert(16)
tree1.insert(1)
tree1.insert(7)
tree1.insert(16)

tree1.print_tree()
print(tree1.find(3).value)
print(tree1.find(10))
tree1.delete_tree()
tree1.print_tree()

# Example 2
tree2 = BST()
tree2.insert(1)
tree2.insert(5)
tree2.insert(7)
tree2.insert(10)
tree2.insert(16)
tree2.insert(16)

tree2.print_tree()
print(tree2.find(3).value)
print(tree2.find(10))
tree2.delete_tree()
tree2.print_tree()
