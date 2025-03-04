"""Дана таблица, состоящая из N строк и M столбцов. В каждой клетке таблицы записано одно из чисел: 0 или 1. Расстоянием между клетками (x1, y1) и (x2, y2) назовем сумму |x1-x2|+|y1-y2|. Вам необходимо построить таблицу, в клетке (i, j) которой будет записано минимальное расстояние между клеткой (i, j) начальной таблицы и клеткой, в которой записана 1. Гарантируется, что хотя бы одна 1 в таблице есть.
Формат ввода

В первой строке вводятся два натуральных числа N и M, не превосходящих 500. Далее идут N строк по M чисел - элементы таблицы.
Формат вывода

Требуется вывести N строк по M чисел - элементы искомой таблицы."""


def table(n, m, a):
    b = [[float("inf")] * m for _ in range(n)]
    queue = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                queue.append((i, j))
                b[i][j] = 0

    while queue:
        x, y = queue.pop(0)
        for dist_x, dist_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_x, n_y = x + dist_x, y + dist_y
            if 0 <= n_x < n and 0 <= n_y < m and b[n_x][n_y] > b[x][y] + 1:
                b[n_x][n_y] = b[x][y] + 1
                queue.append((n_x, n_y))
    return b


n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
print("\n".join(" ".join(map(str, row)) for row in table(n, m, a)))
