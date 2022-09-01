# hard, famous algorithms
# # time O(v^2 + e) | space O(v)
def dijkstrasAlgorithm(start, edges):
    paths = [float('inf')] * len(edges)
    paths[start] = 0
    visited = set()
    while len(visited) < len(edges):
        minNode = None
        for i in range(len(paths)):
            if i not in visited and paths[i] != -1 and (minNode is None or paths[i] < paths[minNode]):
                minNode = i
        if minNode is None:
            break
        visited.add(minNode)
        for dest, length in edges[minNode]:
            paths[dest] = min(paths[dest], paths[minNode] + length)
    return list(map(lambda d: -1 if d == float('inf') else d, paths))
