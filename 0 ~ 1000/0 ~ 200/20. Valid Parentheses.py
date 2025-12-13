"""250914"""


# 堆疊: 第一次測試通過版本
def isValid(self, s: str) -> bool:
    stack = []

    for b in s:
        if not stack:
            stack.append(b)
        elif b == "}" and stack[-1] == "{":
            stack.pop()
        elif b == "]" and stack[-1] == "[":
            stack.pop()
        elif b == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(b)

    if stack:
        return False
    else:
        return True


# 修正版
def isValid(self, s: str) -> bool:
    stack = []
    mapping = {"}": "{", "]": "[", ")": "("}

    for char in s:
        if char in mapping.values():  # 如果是左括號
            stack.append(char)
        elif char in mapping:  # 如果右括號
            # 如果堆疊為空，或者最近的括號不是對應的左括號，代表無效
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return not stack
