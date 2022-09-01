# medium, strings
# time O(1) | space O(1)
def validIPAddresses(string):
    addressList = []
    for i in range(27):
        p1 = i // 9 % 3 + 1
        p2 = i // 3 % 3 + 1 + p1
        p3 = i // 1 % 3 + 1 + p2
        if p3 > len(string) - 1:
            continue
        ranges = [(0, p1), (p1, p2), (p2, p3), (p3, len(string))]
        parts = [string[left:right] for left, right in ranges]
        if all([isValid(part) for part in parts]):
            addressList.append('.'.join(parts))
    return addressList

def isValid(part):
    return not((len(part) > 1 and part[0] == '0') or int(part) > 255)
