# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).

def graph_maker(n):
    res = {}
    n_while = 0

    while n_while < n:
        i = int(input(f'Сколько стрелок отходит от вершины {n_while + 1}: '))
        res[n_while + 1] = list(int(input(f'{el}й связанный элемент: ')) for el in range(1, i + 1))
        n_while += 1

    return res


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)

        for el in graph[node]:
            dfs(graph, el, visited)

    return visited


grph_param = int(input('Сколько будет вершин?: '))
grph = graph_maker(grph_param)
start = int(input('От какой вершины пойдём?: '))  # сделала вариант, где вершины обозначаются цифрами
print(grph)

visited = dfs(grph, start,  [])
print('Путь:')
print(visited)

# 1 пример
# Сколько будет вершин?: 5
# От какой вершины пойдём?: 1
# Сколько стрелок отходит от вершины 1: 1
# 1й связанный элемент: 5
# Сколько стрелок отходит от вершины 2: 2
# 1й связанный элемент: 4
# 2й связанный элемент: 5
# Сколько стрелок отходит от вершины 3: 1
# 1й связанный элемент: 1
# Сколько стрелок отходит от вершины 4: 3
# 1й связанный элемент: 1
# 2й связанный элемент: 2
# 3й связанный элемент: 4
# Сколько стрелок отходит от вершины 5: 1
# 1й связанный элемент: 3
# {1: [5], 2: [4, 5], 3: [1], 4: [1, 2, 4], 5: [3]}
# Путь:
# [1, 5, 3]
# комментарий: если идём от 1 в описанном ниже графе, то, не совершив петлю,
# можно будет пройти только через 3 вершины

# 2 пример
# Сколько будет вершин?: 5
# От какой вершины пойдём?: 1
# Сколько стрелок отходит от вершины 1: 2
# 1й связанный элемент: 2
# 2й связанный элемент: 3
# Сколько стрелок отходит от вершины 2: 3
# 1й связанный элемент: 1
# 2й связанный элемент: 2
# 3й связанный элемент: 5
# Сколько стрелок отходит от вершины 3: 1
# 1й связанный элемент: 4
# Сколько стрелок отходит от вершины 4: 1
# 1й связанный элемент: 5
# Сколько стрелок отходит от вершины 5: 1
# 1й связанный элемент: 3
# {1: [2, 3], 2: [1, 2, 5], 3: [4], 4: [5], 5: [3]}
# Путь:
# [1, 2, 5, 3, 4]

# 3 пример
# Сколько будет вершин?: 5
# От какой вершины пойдём?: 3
# Сколько стрелок отходит от вершины 1: 1
# 1й связанный элемент: 2
# Сколько стрелок отходит от вершины 2: 2
# 1й связанный элемент: 2
# 2й связанный элемент: 4
# Сколько стрелок отходит от вершины 3: 2
# 1й связанный элемент: 1
# 2й связанный элемент: 5
# Сколько стрелок отходит от вершины 4: 1
# 1й связанный элемент: 5
# Сколько стрелок отходит от вершины 5: 1
# 1й связанный элемент: 1
# {1: [2], 2: [2, 4], 3: [1, 5], 4: [5], 5: [1]}
# Путь:
# [3, 1, 2, 4, 5]
