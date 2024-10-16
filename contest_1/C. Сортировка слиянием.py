# Отсортируйте данный массив, используя сортировку слиянием.
# Формат ввода

# Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее идет N целых чисел, не превосходящих по абсолютной величине 109.
# Формат вывода

# Выведите эти числа в порядке неубывания.

def merge_sort(N):
    if len(N) == 1:
        return N
    else:
        mid = len(N) // 2
        left_N, right_N = N[:mid], N[mid:]

        merge_sort(left_N), merge_sort(right_N)
    
        i = j = k = 0

        while i < len(left_N) and j < len(right_N):
            if left_N[i] < right_N[j]:
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

n = int(input())
N = list(map(int, input().split()))
print(*merge_sort(N))