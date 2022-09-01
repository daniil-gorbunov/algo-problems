# medium, recursion
# time O(n*4^n) | space O(n*4^n)
def phoneNumberMnemonics(phoneNumber, idx=0):
    if idx == len(phoneNumber):
        return ['']
    matchedLetters = letters[int(phoneNumber[idx])]
    nextMnemonics = phoneNumberMnemonics(phoneNumber, idx + 1)
    mnemonics = []
    for letter in matchedLetters:
        for mnemonic in nextMnemonics:
            mnemonics.append(letter + mnemonic)
    return mnemonics

letters = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
