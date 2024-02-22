from binaryTree import *
from collections import deque

nodes = deque()
operators = deque()
expressionTree = BinaryTree()

string_input = "(1+2*3)"
test = "(1+2*3)+((4*5+6)*7)"


def run():
    num = ''
    skip = 0
    for i, char in enumerate(string_input):
        if skip > 0:
            skip -= 1
            continue
        if char in "(":
            operators.append(char)
        elif char in "+-":
            """
            check the stack
                - check top node priority
            if priority higher or equal
                - add operator to the stack
            else
                - pull top operator out
                - create subtree with operator
                - push new operator node to node stack
                - keep going until lowered priority
                - add operator to the stack
            """
            try:
                if operators[-1] in "+-(":
                    operators.append(char)
                else:
                    while operators[-1] in "*/":
                        if len(nodes) < 2:
                            print(f"ERROR: Missing operand for {char} at character {i+1}")
                        else:
                            operator = BinaryTreeNode(operators.pop())
                            operator.rightPointer = nodes.pop()
                            operator.leftPointer = nodes.pop()
                            nodes.append(operator)
                    operators.append(char)
            except:
                operators.append(char)
        elif char in "*/":
            try:
                if operators[-1] in "*/+-(":
                    operators.append(char)
                else:
                    while operators[-1] in "*/":
                        if len(nodes) < 2:
                            print(f"ERROR: Missing operand for {char} at character {i+1}")
                        else:
                            operator = BinaryTreeNode(operators.pop())
                            operator.rightPointer = nodes.pop()
                            operator.leftPointer = nodes.pop()
                            nodes.append(operator)
                    operators.append(char)
            except:
                operators.append(char)
        elif char in ")":
            if "(" not in operators:
                print(f"ERROR: Missing open '(' for character {i+1}")
            else:
                while operators[-1] not in "(":
                    operator = BinaryTreeNode(operators.pop())
                    operator.rightPointer = nodes.pop()
                    operator.leftPointer = nodes.pop()
                    nodes.append(operator)
                operators.pop()
        elif char in "0123456789.":
            num += char
            j = 1
            try:
                while string_input[i+j] in "0123456789.":
                    num += string_input[i+j]
                    j += 1
            except:
                pass
            nodes.append(BinaryTreeNode(float(num)))
            skip += j - 1
            num = ''
        else:
            print(f"Can't recognize character [{i+1}]")
            exit()
        # print(operators)
        # for node in nodes:
        #     try:
        #         print(node.value, node.leftPointer.value, node.rightPointer.value)
        #     except:
        #         print(node.value, node.leftPointer, node.rightPointer)
    if len(operators) != 0:
        print("ERROR: Missing operands for remainding operators")
    else:
        expressionTree.root = nodes.pop()
        # print(expressionTree.root.value)
        expressionTree.inOrderTraversal(expressionTree.root)


if __name__ == "__main__":
    run()
    # print(operators)
    # for node in nodes:
    #     try:
    #         print(node.value, node.leftPointer.value, node.rightPointer.value)
    #     except:
    #         print(node.value, node.leftPointer, node.rightPointer)