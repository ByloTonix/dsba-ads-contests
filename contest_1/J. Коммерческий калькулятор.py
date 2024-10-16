class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, k):
        return (k - 1) // 2

    def left_child(self, k):
        return 2 * k + 1

    def right_child(self, k):
        return 2 * k + 2

    def insert(self, value):
        self.heap.append(value)
        self.shift_up(len(self.heap) - 1)

    def shift_up(self, k):
        while k > 0 and self.heap[self.parent(k)] > self.heap[k]:
            self.heap[self.parent(k)], self.heap[k] = (
                self.heap[k],
                self.heap[self.parent(k)],
            )
            k = self.parent(k)

    def shift_down(self, k):
        max_index = k
        left_child = self.left_child(k)
        right_child = self.right_child(k)

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[max_index]:
            max_index = left_child

        if (
            right_child < len(self.heap)
            and self.heap[right_child] < self.heap[max_index]
        ):
            max_index = right_child

        if k != max_index:
            self.heap[k], self.heap[max_index] = self.heap[max_index], self.heap[k]
            self.shift_down(max_index)

    def extract(self):
        if len(self.heap) != 0:
            min_value = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            if len(self.heap) > 0:
                self.shift_down(0)
            return min_value
        return None


heap = Heap()
total = 0
n = int(input())
N = list(map(int, input().split()))

for n in N:
    heap.insert(n)

while len(heap.heap) > 1:
    first, second = heap.extract(), heap.extract()
    heap.insert(first + second)
    total += (first + second) * 0.050

print(f"{total:.2f}")
