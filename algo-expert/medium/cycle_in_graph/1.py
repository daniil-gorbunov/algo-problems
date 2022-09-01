# medium, graphs
# time O(v+e) | space O(v)
def cycleInGraph(edges):
    done = set()
    for i in range(len(edges)):
        checking = set()
        if traverse(i, edges, checking, done):
            return True
        done |= checking
    return False

def traverse(i, edges, checking, done):
    if i in checking:
        return True
    checking.add(i)
    for node in edges[i]:
        if node in done:
            continue
        if traverse(node, edges, checking, done):
            return True
    checking.remove(i)
    return False
