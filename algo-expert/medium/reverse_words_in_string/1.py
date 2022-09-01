# medium, strings
# time O(n) | space O(n)
def reverseWordsInString(string):
    reversedParts = []
    right = len(string)
    left = right - 1
    while left >= 0:
        if string[left] == ' ':
            if left < right - 1:
                reversedParts.append(string[left + 1:right])
                right = left + 1
            reversedParts.append(string[left])
            right -= 1
        left -= 1
    reversedParts.append(string[left + 1:right])
    return ''.join(reversedParts)
