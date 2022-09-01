# easy, recursion
# time O(n) | space O(1)
def getNthFib(n):
    fib = [0, 1]
    while n > len(fib):
        temp = fib[0] + fib[1]
        fib[0] = fib[1]
        fib[1] = temp
        n -= 1
    return fib[n - 1]
