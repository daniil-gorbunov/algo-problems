# medium, recursion
def phoneNumberMnemonics(phoneNumber):
    mnemonics = ['']
    for digit in phoneNumber:
        nextMnemonics = []
        for letter in letters[int(digit)]:
            for mnemonic in mnemonics:
                nextMnemonics.append(mnemonic + letter)
        mnemonics = nextMnemonics
    return mnemonics

letters = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
