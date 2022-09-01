# medium, strings
# time O(n^2) | space O(n)
def longestPalindromicSubstring(string):
    longest = [0, 1]
    for mid in range(len(string)):
        left = right = mid
        while right < len(string) and string[left] == string[right]:
            right += 1
        while left > 0 and right < len(string) and string[left - 1] == string[right]:
            left -= 1
            right += 1
        if right - left > longest[1] - longest[0]:
            longest = [left, right]
    return string[longest[0]:longest[1]]
