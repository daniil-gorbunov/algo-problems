# medium, strings
# time O(w*n*log(n)) | space O(wn)
# n - longest word length
# w - words number
def groupAnagrams(words):
    groups = {}
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in groups:
            groups[sortedWord] = []
        groups[sortedWord].append(word)
    return list(groups.values())
