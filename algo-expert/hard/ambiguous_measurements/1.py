# hard, recursion
# time O(l*h*n) | space O(l*h)
def ambiguousMeasurements(cups, low, high):
    return measure(cups, low, high, {})

def measure(cups, low, high, cache, curLow = 0, curHigh = 0):
    key = f'{curLow},{curHigh}'
    if key in cache:
        return cache[key]
    if curLow > high or curHigh > high:
        cache[key] = False
        return False
    if curLow >= low and curHigh <= high:
        return True
    for cup in cups:
        if measure(cups, low, high, cache, curLow + cup[0], curHigh + cup[1]):
            return True
    cache[key] = False
    return False
