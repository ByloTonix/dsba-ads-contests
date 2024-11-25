def process_commands(prompts):
    arr, _arr = [], []

    def insert(arr, s):
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] >= s:
                r = mid
            else:
                l = mid + 1
        arr.insert(l, s)

    for c in prompts:
        try:
            k = int(c) - 1
            _arr.append(arr[k])
        except ValueError:
            insert(arr, c)

    return _arr


print("\n".join(process_commands([input() for _ in range(int(input()))])))
