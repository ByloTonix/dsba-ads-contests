# Палиндром — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях.
# На вход программы поступает набор больших латинских букв. Разрешается переставлять и удалять буквы. Требуется из данных букв составить палиндром наибольшей длины. Если таких палиндромов несколько, то выбрать первый из них в алфавитном порядке.
# Формат ввода

# В первой строке входных данных содержится число N (1 <= N <= 100000). Во второй строке задается последовательность из N больших латинских букв.
# Формат вывода

# Выдайте искомый палиндром.


def merge_sort(N, reversed=False):
    if len(N) <= 1:
        return N
    else:
        mid = len(N) // 2
        left_N, right_N = N[:mid], N[mid:]

        merge_sort(left_N, reversed), merge_sort(right_N, reversed)

        i = j = k = 0

        while i < len(left_N) and j < len(right_N):
            if (left_N[i] < right_N[j] and not reversed) or (
                left_N[i] > right_N[j] and reversed
            ):
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


# n = int(input())
# N = [_ for _ in input()]

# print("".join(merge_sort(N[:len(N)//2], reversed=False) + merge_sort(N[len(N)//2:], reversed=True)))

n = int(input())
N = merge_sort([_ for _ in input()])

L, half, mid = {}, [], ""

for l in N:
    if l in L:
        L[l] += 1
    else:
        L[l] = 1

for c in merge_sort(list(L.keys())):
    if L[c] % 2 == 0:
        half.append((L[c] // 2) * c)
    else:
        half.append((L[c] // 2) * c)
        if mid == "":
            mid = c
# print(half, mid)
half = "".join(half)
last_half = "".join(merge_sort(list(half), reversed))
p = half + mid + last_half

print(p)
