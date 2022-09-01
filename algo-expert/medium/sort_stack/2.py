# medium, stacks
# time O(n^2) | space O(n)
def sortStack(stack):
    if not stack:
        return stack
    topVal = stack.pop()
    sortStack(stack)
    insert(stack, topVal)
    return stack

def insert(stack, val):
    if not stack or stack[-1] <= val:
        stack.append(val)
    else:
        topVal = stack.pop()
        insert(stack, val)
        stack.append(topVal)
