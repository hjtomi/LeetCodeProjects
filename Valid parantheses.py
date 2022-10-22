def is_valid(s):
    stack = []
    dir = {")": "(", "]": "[", "}": "{"}
    for bracket in s:
        if bracket not in dir.keys():
            stack.append(bracket)
        elif bracket in dir.keys():
            if len(stack) == 0:
                return False
            elif stack.pop() != dir[bracket]:
                return False
    return not stack


print(is_valid("()"))
