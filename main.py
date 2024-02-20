from binaryTree import *

tree = BinaryTree()

tree.root = BinaryTreeNode(3)

tree.insert(2)
tree.insert(1)
tree.insert(5)
tree.insert(4)
tree.insert(9)

tree.inOrderTraversal(tree.root)
print()
tree.remove(5, tree.root)
tree.inOrderTraversal(tree.root)