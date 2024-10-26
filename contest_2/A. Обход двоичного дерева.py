def in_order(n, k):
    if tree[n][1] != -1:
        in_order(tree[n][1], k)
    k.append(tree[n][0])
    if tree[n][2] != -1:
        in_order(tree[n][2], k)


def pre_order(n, k):
    k.append(tree[n][0])
    if tree[n][1] != -1:
        pre_order(tree[n][1], k)
    if tree[n][2] != -1:
        pre_order(tree[n][2], k)


def post_order(n, k):
    if tree[n][1] != -1:
        post_order(tree[n][1], k)
    if tree[n][2] != -1:
        post_order(tree[n][2], k)
    k.append(tree[n][0])


tree = []
for i in range(int(input())):
    tree.append([int(s) for s in input().split()])

inorder, preorder, postorder = [], [], []

in_order(0, inorder), pre_order(0, preorder), post_order(0, postorder)

print(" ".join(map(str, inorder)))
print(" ".join(map(str, preorder)))
print(" ".join(map(str, postorder)))