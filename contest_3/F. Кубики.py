def petya(n, m, c):
    c += c[:n][::-1]
    possible = [0] * (2 * n)
    for i in range(1, 2 * n):
        j = possible[i - 1]
        while j > 0 and c[i] != c[j]:
            j = possible[j - 1]
        if c[i] == c[j]:
            j += 1
        possible[i] = j

    length = possible[-1]
    while length > n:
        length = possible[length - 1]

    answer = []
    while length > 0:
        if length % 2 == 0:
            answer.append(n - length // 2)
        length = possible[length - 1]
    answer.append(n)
    return sorted(answer)


n, m = map(int, input().split())
c = list(map(int, input().split()))
result = petya(n, m, c)
print(*result)
