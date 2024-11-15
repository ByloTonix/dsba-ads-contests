def z(S):
    n = len(S)
    Z, l, r = [0] * n, 0, 0
    Z[0] = n
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while (Z[i] + i < n) and (S[Z[i]] == S[Z[i] + i]):
            Z[i] += 1
        if Z[i] + i - 1 > r:
            l, r = i, Z[i] + i - 1
    return Z


print(*z(input()))
