from copy import deepcopy

class BinaryTreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.rightPointer = None
        self.leftPointer = None


class BinaryTree:
    def __init__(self, root:BinaryTreeNode=None):
        self.root = root

    def findMin(self, node:BinaryTreeNode) -> BinaryTreeNode:
        if self.isEmpty():
            return None
        if node.leftPointer is not None:
            return self.findMin(node.leftPointer)
        return node

    def findMax(self, node:BinaryTreeNode) -> BinaryTreeNode:
        if self.isEmpty():
            return None
        if node.rightPointer is not None:
            return self.findMax(node.rightPointer)
        return node

    def find(self, item, node:BinaryTreeNode) -> bool:
        if self.isEmpty():
            return False
        if node is None:
            return False
        if item == node.value:
            return node
        if item < node.value:
            return self.find(item, node.leftPointer)
        if item > node.value:
            return self.find(item, node.rightPointer)

    def isEmpty(self) -> bool:
        if self.root is  None:
            return True
        return False

    def insert(self, item, node:BinaryTreeNode=None) -> None:
        if node is None:
            if self.root is None:
                self.root = BinaryTreeNode(item)
                return
            node = self.root
        if item < node.value:
            if node.leftPointer is None:
                node.leftPointer = BinaryTreeNode(item, node)
            else:
                self.insert(item, node.leftPointer)
        if item >= node.value:
            if node.rightPointer is None:
                node.rightPointer = BinaryTreeNode(item, node)
            else:
                self.insert(item, node.rightPointer)

    def remove(self, item, node:BinaryTreeNode) -> None:
        if node is None:
            return
        if item < node.value:
            self.remove(item, node.leftPointer)
        elif item > node.value:
            self.remove(item, node.rightPointer)
        else:
            print(f"removed: {node.value}")
            if node.rightPointer is None and node.leftPointer is None:
                if node is node.parent.rightPointer:
                    node.parent.rightPointer = None
                else:
                    node.parent.leftPointer = None
            elif node.rightPointer and node.leftPointer is None:
                if node is node.parent.rightPointer:
                    node.rightPointer.parent = node.parent
                    node.parent.rightPointer = node.rightPointer
                else:
                    node.rightPointer.parent = node.parent
                    node.parent.leftPointer = node.rightPointer
            elif node.leftPointer and node.rightPointer is None:
                if node is node.parent.rightPointer:
                    node.leftPointer.parent = node.parent
                    node.parent.rightPointer = node.leftPointer
                else:
                    node.leftPointer.parent = node.parent
                    node.parent.leftPointer = node.leftPointer
            else:
                minNode = deepcopy(self.findMin(node.rightPointer))
                minNode.parent = node.parent
                node.leftPointer.parent = minNode
                minNode.leftPointer = node.leftPointer
                node.rightPointer.parent = minNode
                minNode.rightPointer = node.rightPointer
                if node is node.parent.rightPointer:
                    node.parent.rightPointer = minNode
                    self.remove(minNode.value, minNode.rightPointer)
                else:
                    node.parent.leftPointer = minNode
                    self.remove(minNode.value, minNode.rightPointer)

    def inOrderTraversal(self, node:BinaryTreeNode) -> None:
        if node is not None:
            self.inOrderTraversal(node.leftPointer)
            # print(f"node: {node.value} | rp: {node.rightPointer.value if node.rightPointer else None} {'   ' if node.rightPointer else ''}| lp: {node.leftPointer.value if node.leftPointer else None} {'   ' if node.leftPointer else ''}| parent: {node.parent.value if node.parent else None}")
            print(node.value)
            self.inOrderTraversal(node.rightPointer)

    def preOrderTraversal(self, node:BinaryTreeNode) -> None:
        if node is not None:
            print(node.value)
            self.preOrderTraversal(node.leftPointer)
            self.preOrderTraversal(node.rightPointer)

    def postOrderTraversal(self, node:BinaryTreeNode) -> None:
        if node is not None:
            self.postOrderTraversal(node.leftPointer)
            self.postOrderTraversal(node.rightPointer)
            print(node.value)

    def treeHeight(self, node:BinaryTreeNode) -> int:
        if node is None:
            return -1
        else:
            return 1 + self.larger(self.treeHeight(node.leftPointer), self.treeHeight(node.rightPointer))

    def treeNodeCount(self, node:BinaryTreeNode) -> int:
        if node is None:
            return 0
        return 1 + self.treeNodeCount(node.leftPointer) + self.treeNodeCount(node.rightPointer)

    def treeLeaveCount(self, node:BinaryTreeNode) -> int:
        if node is None:
            return 0
        elif node.leftPointer is None and node.rightPointer is None:
            return 1
        elif node.leftPointer is None:
            return self.treeLeaveCount(node.rightPointer)
        elif node.rightPointer is None:
            return self.treeLeaveCount(node.leftPointer)
        else:
            return self.treeLeaveCount(node.rightPointer) + self.treeLeaveCount(node.leftPointer)

    def larger(self, x:int, y:int):
        return x if x >= y else y