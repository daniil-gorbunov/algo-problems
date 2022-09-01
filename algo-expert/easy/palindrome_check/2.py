# easy, strings
# time O(n) | space O(n)
def isPalindrome(str, left=0):
    right = len(str) - left - 1
    return True if left >= right else str[left] == str[right] and isPalindrome(str, left + 1)
