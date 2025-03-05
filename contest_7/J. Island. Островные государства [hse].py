"""Суровые феодальные времена переживала некогда великая островная страна Байтландия. 
За главенство над всем островом борются два самых сильных барона. Таким образом, каждый город страны контролируется одним из правителей. 
Как водится издревле, некоторые из городов соединены двусторонними дорогами. Бароны очень не любят друг друга и стараются делать как можно больше пакостей. 
В частности, теперь для того чтобы пройти по дороге, соединяющей города различных правителей, надо заплатить пошлину — один байтландский рубль.

Программист Вася живет в городе номер 1. С наступлением лета он собирается съездить в город N на Всебайтландское сборище программистов. 
Разумеется, он хочет затратить при этом как можно меньше денег и помочь ему здесь, как обычно, предлагается Вам.

Формат ввода

В первой строке входного файла записано два числа N и M (1 ≤ N, M ≤ 100000) — количество городов и количество дорог соответственно.
В следующий строке содержится информация о городах — N чисел 1 или 2 — какому из баронов принадлежит соответствующий город.
В последних M строках записаны пары 1 ≤ a, b ≤ N, a ≠ b. Каждая пара означает наличие дороги из города a в город b. По дорогам Байтландии можно двигаться в любом направлении.

Формат вывода

Если искомого пути не существует, выведите единственное слово impossible. В противном случае в первой строке напишите минимальную стоимость и количество посещенных городов, 
а во вторую выведите эти города в порядке посещения. Если минимальных путей несколько, выведите любой.
"""

import heapq


def bytebaron(n, m, owners, roads):
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dist = [float("inf")] * (n + 1)
    dist[1] = 0
    parent = [-1] * (n + 1)

    nodes = [(0, 1)]

    while nodes:
        cost, city = heapq.heappop(nodes)

        if cost > dist[city]:
            continue

        for neighbor in graph[city]:
            new_cost = cost
            if owners[city - 1] != owners[neighbor - 1]:
                new_cost += 1

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                parent[neighbor] = city
                heapq.heappush(nodes, (new_cost, neighbor))

    if dist[n] == float("inf"):
        return "impossible"

    path, curr = [], n
    while curr != -1:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    return dist[n], len(path), path


n, m = map(int, input().split())
cities = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(m)]

result = bytebaron(n, m, cities, roads)

if result == "impossible":
    print("impossible")
else:
    print(result[0], result[1])
    print(" ".join(map(str, result[2])))
