import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, dex, a, b):
        self.dex, self.a, self.b, self.left, self.right, self.parent = (
            dex,
            a,
            b,
            None,
            None,
            None,
        )


def build(nodes):
    root = nodes[0]
    last_element = root

    for i in range(1, len(nodes)):
        if last_element.b < nodes[i].b:
            last_element.right = nodes[i]
            nodes[i].parent = last_element
            last_element = last_element.right
        else:
            current = last_element
            while current.parent != None and current.b > nodes[i].b:
                current = current.parent
            if current.b > nodes[i].b:
                nodes[i].left = current
                nodes[i].parent = current.parent
                if current.parent != None:
                    current.parent.right = nodes[i]
                current.parent = nodes[i]
            else:
                nodes[i].left = current.right
                if current.right != None:
                    current.right.parent = nodes[i]
                current.right = nodes[i]
                nodes[i].parent = current
            last_element = nodes[i]

    while last_element.parent != None:
        last_element = last_element.parent
    return last_element


def check_bst(node, last_a=[float("-inf")]):
    if node.left:
        if not check_bst(node.left, last_a):
            return False
    if node.a <= last_a[0]:
        return False
    last_a[0] = node.a
    if node.right:
        if not check_bst(node.right, last_a):
            return False
    return True


def check_heap(node):
    if node.left:
        if node.b > node.left.b or not check_heap(node.left):
            return False

    if node.right:
        if node.b > node.right.b or not check_heap(node.right):
            return False
    return True


def printn(nodes):
    nodes.sort(key=lambda node: node.dex)
    print("YES")
    for node in nodes:
        print(
            node.parent.dex if node.parent else 0,
            node.left.dex if node.left else 0,
            node.right.dex if node.right else 0,
        )


n = int(input())
vertices = [Node(i + 1, *map(int, input().split())) for i in range(n)]

temp, tmp = {node.a for node in vertices}, {node.b for node in vertices}
if len(tmp) != n or len(temp) != n:
    print("NO")
    exit()

vertices.sort(key=lambda node: node.a)
root = build(vertices)

if not (check_bst(root) and check_heap(root)):
    print("NO")
    exit()

printn(vertices)
