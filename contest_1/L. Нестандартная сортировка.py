def SelectionSort(A, order):
    arr = [(i, order[i]) for i in A]

    for i in range(len(arr) - 1):
        _min = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] < arr[_min][1]:
                _min = j
        arr[i], arr[_min] = arr[_min], arr[i]
    return ''.join(a for a, _ in arr)



s, t = input().strip(), input().strip()

c = {b: a for a, b in enumerate(s)}
print("".join(SelectionSort(t, c)))
