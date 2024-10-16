def recursive(arr, n, i):
    _max, l = i, i + i + 1
    r = l + 1

    if l < n and arr[l] > arr[_max]:
        _max = l
    if r < n and arr[r] > arr[_max]:
        _max = r
    if _max != i:
        arr[i], arr[_max] = arr[_max], arr[i]
        recursive(arr, n, _max)

def heap_sort(arr):
    el = len(arr) // 2 - 1
    for i in range(el, -1, -1):
        recursive(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        recursive(arr, i, 0)

    return arr

n = int(input())
print(*heap_sort(list(map(int, input().split()))))