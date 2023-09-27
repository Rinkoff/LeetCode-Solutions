"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def isValid(s: str) -> bool:
    brackets = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack:
                return False
            elif stack.pop() != brackets[char]:
                return False
        else:
            return False
    return not stack

s = "()[]{}"

print(isValid(s))