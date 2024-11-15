def z_to_pi(Z):
    n = len(Z)
    P = [0] * n

    for i in range(1, n):
        if Z[i] > 0:
            j = Z[i] - 1
            while j >= 0 and P[i + j] == 0:
                P[i + j] = j + 1
                j -= 1

    return P


n = int(input())
print(*z_to_pi(list(map(int, input().split()))))
