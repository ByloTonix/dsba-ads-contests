from random import randint as ran

class Vertex:
    def __init__(self, key):
        self.key, self.rank, self.left, self.right, self.total, self.count = (
            key,
            ran(1, 1000000000),
            None,
            None,
            key,
            1,
        )


class TreeStruct:
    def __init__(self):
        self.base = None

    def _get_count(self, vert):
        return vert.count if vert else 0

    def _get_total(self, vert):
        return vert.total if vert else 0

    def _update(self, vert):
        if vert:
            vert.count, vert.total = 1 + self._get_count(vert.left) + self._get_count(
                vert.right
            ), vert.key + self._get_total(vert.left) + self._get_total(vert.right)
        return vert

    def _split(self, vert, key):
        if not vert:
            return None, None
        if vert.key < key:
            vert.right, right = self._split(vert.right, key)
            return self._update(vert), right
        else:
            left, vert.left = self._split(vert.left, key)
            return left, self._update(vert)

    def _merge(self, left, right):
        if not left or not right:
            return left or right
        if left.rank > right.rank:
            left.right = self._merge(left.right, right)
            return self._update(left)
        else:
            right.left = self._merge(left, right.left)
            return self._update(right)

    def insert(self, key):
        if not self.search(key):
            new_node, left, right = Vertex(key), *self._split(self.base, key)
            self.base = self._merge(self._merge(left, new_node), right)

    def erase(self, key):
        if self.search(key):
            left, mid = self._split(self.base, key)
            mid, right = self._split(mid, key + 1)
            self.base = self._merge(left, right)

    def search(self, key):
        vert = self.base
        while vert:
            if vert.key == key:
                return True
            vert = vert.right if vert.key < key else vert.left
        return False

    def range_total(self, min_key, max_key):
        left, mid = self._split(self.base, min_key)
        mid, right = self._split(mid, max_key + 1)
        result = self._get_total(mid)
        self.base = self._merge(self._merge(left, mid), right)
        return result


class UniqueSetStruct:
    def __init__(self):
        self.treap, self.last_total = TreeStruct(), 0

    def transform(self, x):
        return (x + self.last_total) % 1000000001

    def insert(self, elem):
        self.treap.insert(self.transform(elem))

    def erase(self, elem):
        self.treap.erase(self.transform(elem))

    def contains(self, elem):
        print("Found" if self.treap.search(self.transform(elem)) else "Not found")

    def total_range(self, left, right):
        min_key, max_key = sorted([self.transform(left), self.transform(right)])
        self.last_total = self.treap.range_total(min_key, max_key)
        print(self.last_total)


dataset = UniqueSetStruct()
for _ in range(int(input())):
    cmd = input().split()
    (
        dataset.insert(int(cmd[1]))
        if cmd[0] == "+"
        else (
            dataset.erase(int(cmd[1]))
            if cmd[0] == "-"
            else (
                dataset.contains(int(cmd[1]))
                if cmd[0] == "?"
                else dataset.total_range(int(cmd[1]), int(cmd[2]))
            )
        )
    )
