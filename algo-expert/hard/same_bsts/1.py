# hard, BST
# time O(n^2) | space O(n^2)
def sameBsts(arr1, arr2):
    if not arr1 and not arr2:
        return True
    if len(arr1) != len(arr2) or arr1[0] != arr2[0]:
        return False
    if all([arr1[i] == arr2[i] for i in range(1, len(arr1))]):
        return True
    left1, right1 = getBranches(arr1)
    left2, right2 = getBranches(arr2)
    return sameBsts(left1, left2) and sameBsts(right1, right2)

# time O(n) | space O(n)
def getBranches(arr):
    left, right = [], []
    for i in range(1, len(arr)):
        branch = left if arr[i] < arr[0] else right
        branch.append(arr[i])
    return left, right
