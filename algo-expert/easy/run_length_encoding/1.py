# easy, strings
# time O(n) | space O(n)
def runLengthEncoding(s):
    result = []
    counter = 1
    for i in range(1, len(s)):
        if counter == 9 or s[i] != s[i - 1]:
            result.extend([str(counter), s[i - 1]])
            counter = 0
        counter += 1
    result.extend([str(counter), s[-1]])
    return ''.join(result)
