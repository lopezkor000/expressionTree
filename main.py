from binaryTree import *
from collections import deque

nodes = deque()
operators = deque()
expressionTree = BinaryTree()

# string_input = "(1+2*3)+((4*5+6)*7)"
string_input = "10"


def run():
    num = None
    skip = 0
    for i, char in enumerate(string_input):
        if skip > 0:
            skip -= 1
            continue
        print(char)
        if char == "(":
            operators.append(char)
        elif char == "+" or char == "-":
            # do something
            pass
        elif char == "*" or char == "/":
            # do something
            pass
        elif char == ")":
            pass
        elif char in "0123456789.":
            num = char
            j = 0
            while True:
                try:
                    j += 1
                    part = string_input[i+j]
                    if part in "0123456789.":
                        num += part
                    else:
                        break
                except:
                    j -= 1
                    break
            nodes.append(BinaryTreeNode(float(num)))
            print(float(num))
            num = None
            skip = j-1
        else:
            print(f"Can't recognize character [{i}]")
            exit()


if __name__ == "__main__":
    run()
    for node in nodes:
        print(node.value)