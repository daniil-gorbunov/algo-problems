# medium, strings
# time O(wn) | space O(w)
# n - longest word length
# w - words number
primes = [
    2,  3,  5,  7,  11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101
]

def groupAnagrams(words):
    groups = {}
    for word in words:
        hash = 0
        for char in word:
            charPos = ord(char) - ord('a')
            hash += (charPos + 1) * primes[charPos]
        if hash not in groups:
            groups[hash] = []
        groups[hash].append(word)
    return list(groups.values())
