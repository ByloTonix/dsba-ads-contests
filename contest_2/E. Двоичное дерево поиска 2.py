class AVLNode:
    def __init__(self, value):
        self.left_child, self.right_child, self.height, self.size, self.value = (
            None,
            None,
            1,
            1,
            value,
        )


def getHeight(node):
    return node.height if node else 0


def getSize(node):
    return node.size if node else 0


def update(node):
    if node:
        node.height = 1 + max(getHeight(node.left_child), getHeight(node.right_child))
        node.size = 1 + getSize(node.left_child) + getSize(node.right_child)


def rightRotate(z):
    y = z.left_child
    T3 = y.right_child

    y.right_child = z
    z.left_child = T3

    update(z), update(y)

    return y


def leftRotate(z):
    y = z.right_child
    T2 = y.left_child

    y.left_child = z
    z.right_child = T2

    update(z), update(y)

    return y


def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left_child) - getHeight(node.right_child)


def insert(root, key):
    if not root:
        return AVLNode(key)
    elif key < root.value:
        root.left_child = insert(root.left_child, key)
    elif key > root.value:
        root.right_child = insert(root.right_child, key)

    update(root)
    balance = getBalance(root)

    if balance > 1 and key < root.left_child.value:
        return rightRotate(root)

    if balance < -1 and key > root.right_child.value:
        return leftRotate(root)

    if balance > 1 and key > root.left_child.value:
        root.left_child = leftRotate(root.left_child)
        return rightRotate(root)

    if balance < -1 and key < root.right_child.value:
        root.right_child = rightRotate(root.right_child)
        return leftRotate(root)

    return root


def getMinValue(node):
    if node is None or node.left_child is None:
        return node
    return getMinValue(node.left_child)


def delete(root, key):
    if not root:
        return root

    if key < root.value:
        root.left_child = delete(root.left_child, key)
    elif key > root.value:
        root.right_child = delete(root.right_child, key)
    else:
        if not root.left_child:
            return root.right_child
        elif not root.right_child:
            return root.left_child

        temp = getMinValue(root.right_child)
        root.value = temp.value
        root.right_child = delete(root.right_child, temp.value)

    update(root)

    balance = getBalance(root)

    if balance > 1 and getBalance(root.left_child) >= 0:
        return rightRotate(root)

    if balance > 1 and getBalance(root.left_child) < 0:
        root.left_child = leftRotate(root.left_child)
        return rightRotate(root)

    if balance < -1 and getBalance(root.right_child) <= 0:
        return leftRotate(root)

    if balance < -1 and getBalance(root.right_child) > 0:
        root.right_child = rightRotate(root.right_child)
        return leftRotate(root)

    return root


def exists(root, key):
    if not root:
        return False
    if key == root.value:
        return True
    elif key < root.value:
        return exists(root.left_child, key)
    else:
        return exists(root.right_child, key)


def next(root, key):
    x = None
    while root:
        if key < root.value:
            x = root
            root = root.left_child
        else:
            root = root.right_child
    return x


def prev(root, key):
    x = None
    while root:
        if key > root.value:
            x = root
            root = root.right_child
        else:
            root = root.left_child
    return x


def kth(root, k):
    if not root:
        return None

    left = getSize(root.left_child)
    if k == left + 1:
        return root
    elif k <= left:
        return kth(root.left_child, k)
    else:
        return kth(root.right_child, k - left - 1)


root = None

with open("input.txt", "r") as f:
    for line in f:
        command, *x = line.split()
        value = int(x[0]) if x else None

        if command == "insert":
            root = insert(root, value)
        elif command == "delete":
            root = delete(root, value)
        elif command == "exists":
            print("true" if exists(root, value) else "false")
        elif command == "next":
            succ = next(root, value)
            print(succ.value if succ else "none")
        elif command == "prev":
            pred = prev(root, value)
            print(pred.value if pred else "none")
        elif command == "kth":
            node = kth(root, value)
            print(node.value if node else "none")
