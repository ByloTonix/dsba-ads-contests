def suffix_array(s):
    n = len(s)
    arr = list(range(n))
    rank, _rank = [ord(_) for _ in s], [0] * n
    exp = 1

    while exp < n:
        arr.sort(key=lambda x: (rank[x], rank[x + exp] if x + exp < n else -1))

        _rank[arr[0]] = 0
        for i in range(1, n):
            j, k = arr[i], arr[i - 1]
            if (rank[k], rank[k + exp] if k + exp < n else -1) == \
               (rank[j], rank[j + exp] if j + exp < n else -1):
                _rank[j] = _rank[k]
            else:
                _rank[j] = _rank[k] + 1

        rank, _rank = _rank, rank
        exp *= 2

    return [i + 1 for i in arr]

print(*suffix_array(input()))
