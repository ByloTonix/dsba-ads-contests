def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def simplifier(num, den):
    div = gcd(num, den)
    return (num // div, den // div)


def merge_sort(N):
    if len(N) == 1:
        return N
    else:
        mid = len(N) // 2
        left_N, right_N = N[:mid], N[mid:]

        merge_sort(left_N), merge_sort(right_N)

        i = j = k = 0

        while i < len(left_N) and j < len(right_N):
            if left_N[i][0] * right_N[j][1] < right_N[j][0] * left_N[i][1]:
                N[k] = left_N[i]
                i += 1
            else:
                N[k] = right_N[j]
                j += 1
            k += 1
        while i < len(left_N):
            N[k] = left_N[i]
            i += 1
            k += 1
        while j < len(right_N):
            N[k] = right_N[j]
            j += 1
            k += 1

    return N


n, q = map(int, input().split())
a, b, c = (
    list(map(int, input().split())),
    list(map(int, input().split())),
    list(map(int, input().split())),
)
w = []

for a_i in a:
    for b_j in b:
        w.append(simplifier(a_i, b_j))

merge_sort(w)

for i in c:
    print(*w[i - 1])
