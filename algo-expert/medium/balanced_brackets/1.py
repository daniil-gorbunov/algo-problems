# medium, stacks
# time O(n) | space O(n)
def balancedBrackets(string):
    stack = []
    bracketMatch = {'(': ')', '[': ']', '{': '}'}
    openingBrackets = {'(', '[', '{'}
    closingBrackets = {')', ']', '}'}
    for bracket in string:
        if bracket in openingBrackets:
            stack.append(bracket)
        elif bracket in closingBrackets and (not stack or bracketMatch[stack.pop()] != bracket):
            return False
    return len(stack) == 0
