# hard, stacks
# time O(n) | space O(n)
def shortenPath(path):
    parts = path.split('/')
    stack = []
    for part in parts:
        if part == '':
            if len(stack) != 0:
                continue
            stack.append(part)
        elif part == '.':
            continue
        elif part == '..':
            if len(stack) == 0 or stack[-1] == '..':
                stack.append(part)
            elif stack[-1] == '':
                continue
            else:
                stack.pop(-1)
        else:
            stack.append(part)
    return '/' if len(stack) == 1 and stack[0] == '' else '/'.join(stack)
