# hard, strings
# time O(N) | space O(L)
def longestSubstringWithoutDuplication(str):
    longest = (0, 1)
    usedChars = set()
    left = right = 0
    while right < len(str):
        rightChar = str[right]
        if rightChar in usedChars:
            if right - left > longest[1] - longest[0]:
                longest = (left, right)
            while rightChar in usedChars:
                usedChars.remove(str[left])
                left += 1
        usedChars.add(rightChar)
        right += 1
    if right - left > longest[1] - longest[0]:
        longest = (left, right)
    return str[longest[0]:longest[1]]
