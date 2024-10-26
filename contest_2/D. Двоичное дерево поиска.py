class AVLNode:
    def __init__(self, value):
        self.value, self.left_child, self.right_child, self.height = (
            value,
            None,
            None,
            1,
        )


def insert(root, key):
    if not root:
        return AVLNode(key)
    elif key < root.value:
        root.left_child = insert(root.left_child, key)
    elif key > root.value:
        root.right_child = insert(root.right_child, key)

    root.height = 1 + max(getHeight(root.left_child), getHeight(root.right_child))
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

    if not root:
        return root

    root.height = 1 + max(getHeight(root.left_child), getHeight(root.right_child))
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


def getHeight(root):
    if not root:
        return 0
    return root.height


def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left_child) - getHeight(root.right_child)


def leftRotate(z):
    y = z.right_child
    T2 = y.left_child
    y.left_child = z
    z.right_child = T2
    z.height = 1 + max(getHeight(z.left_child), getHeight(z.right_child))
    y.height = 1 + max(getHeight(y.left_child), getHeight(y.right_child))
    return y


def rightRotate(z):
    y = z.left_child
    T3 = y.right_child
    y.right_child = z
    z.left_child = T3
    z.height = 1 + max(getHeight(z.left_child), getHeight(z.right_child))
    y.height = 1 + max(getHeight(y.left_child), getHeight(y.right_child))
    return y


def getMinValue(root):
    if root is None or root.left_child is None:
        return root
    return getMinValue(root.left_child)


root = None

with open("input.txt", "r") as f:
    for line in f:
        command, x = line.split()
        value = int(x)

        if command == "insert":
            root = insert(root, value)
        elif command == "delete":
            root = delete(root, value)
        elif command == "exists":
            if exists(root, value):
                print("true")
            else:
                print("false")
