def bst(tree, dex, _min, _max):
    key, left, right = tree[dex]

    if dex == -1:
        return True
    if not (_min < key < _max):
        return False

    return bst(tree, left, _min, key) and bst(tree, right, key, _max)


def check(tree):
    return "CORRECT" if bst(tree, 0, -(2**31), 2**31 - 1) else "INCORRECT"


tree = []
n = int(input())
for i in range(n):
    key, left, right = map(int, input().split())
    tree.append((key, left, right))

print(check(tree))
