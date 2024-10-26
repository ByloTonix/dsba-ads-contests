import sys

sys.setrecursionlimit(10**6)


def bst(tree, dex, min_key, max_key):
    if dex == -1:
        return True

    key, left, right = tree[dex]
    if key < min_key or key > max_key:
        return False

    return bst(tree, left, min_key, key - 1) and bst(tree, right, key, max_key)


def check(n, tree):
    if n == 0:
        return "CORRECT"

    return "CORRECT" if bst(tree, 0, float("-inf"), float("inf")) else "INCORRECT"


tree = []
n = int(input())
for _ in range(n):
    key, left, right = map(int, input().split())
    tree.append((key, left, right))

print(check(n, tree))
