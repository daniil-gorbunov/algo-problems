# easy, strings
# time O(n) | space O(n)
def caesarCipherEncryptor(string, key):
    result = []
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    symbolIdxMap = {symbol: i for i, symbol in enumerate(alphabet)}
    for symbol in string:
        idx = (symbolIdxMap[symbol] + key) % len(alphabet)
        result.append(alphabet[idx])
    return ''.join(result)
