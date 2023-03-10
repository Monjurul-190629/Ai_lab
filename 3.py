def dfs(grap, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for nex in grap[start] - visited:
        dfs(grap, nex, visited)
    return visited


graph = {'0': {'1', '2'},
         '1': {'0', '3', '4'},
         '2': {'0'},
         '3': {'1'},
         '4': {'2', '3'}}

dfs(graph, '0')
