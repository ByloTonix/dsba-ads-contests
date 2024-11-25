def compute_lcp(s, arr):
    n = len(s)
    rank, lcp = [0] * n, [0] * (n - 1)

    for i in range(n):
        rank[arr[i] - 1] = i

    c = 0
    for i, r in enumerate(rank):
        if r > 0:
            j = arr[r - 1] - 1
            while i + c < n and j + c < n and s[i + c] == s[j + c]:
                c += 1
            lcp[r - 1] = c
            c = max(0, c - 1)

    return lcp


n = int(input())
print(*compute_lcp(input(), list(map(int, input().split()))))
