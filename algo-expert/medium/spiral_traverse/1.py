# medium, arrays
# time O(n * m) | space O(n * m)
def spiralTraverse(a):
    result = []
    n = len(a)
    m = len(a[0])

    horStep = 0
    verStep = 1
    step = 0
    i = 0
    j = -1
    while step < m * n:
        deltaJ = 1 if horStep % 2 == 0 else -1
        deltaI = 1 if verStep % 2 != 0 else -1
        for _ in range(m - horStep):
            j += deltaJ
            result.append(a[i][j])
            step += 1
        horStep += 1

        for _ in range(n - verStep):
            i += deltaI
            result.append(a[i][j])
            step += 1
        verStep += 1

    return result
