# medium, arrays
# time O(n) | space O(n)
def arrayOfProducts(arr):
    products = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        products[i] =  products[i - 1] * arr[i - 1]
    tempProd = 1
    for i in reversed(range(len(arr))):
        products[i] *= tempProd
        tempProd *= arr[i]
    return products
