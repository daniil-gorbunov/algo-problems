# hard, BST
# time O(n^2) | space O(d)
def sameBsts(arr1, arr2, root1=0, root2=0, minVal=float('-inf'), maxVal=float('inf')):
    print(root1, root2, minVal, maxVal)
    if root1 == -1 or root2 == -1:
        return root1 == root2
    if arr1[root1] != arr2[root2]:
        return False

    left1 = getLeft(arr1, root1, minVal)
    right1 = getRight(arr1, root1, maxVal)
    left2 = getLeft(arr2, root2, minVal)
    right2 = getRight(arr2, root2, maxVal)

    return sameBsts(arr1, arr2, left1, left2, minVal, arr1[root1]) and sameBsts(arr1, arr2, right1, right2, arr1[root1], maxVal)

# time O(n) | space O(1)
def getLeft(arr, root, minVal):
    for i in range(root + 1, len(arr)):
        if arr[i] < arr[root] and arr[i] >= minVal:
            return i
    return -1

# time O(n) | space O(1)
def getRight(arr, root, maxVal):
    for i in range(root + 1, len(arr)):
        if arr[i] >= arr[root] and arr[i] < maxVal:
            return i
    return -1
