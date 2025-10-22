"""251022"""


# FT: Using min()
class MinStack:
    def __init__(self):
        self.stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Double Stack
class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.min_stack[-1] == self.stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
        else:
            return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Single Stack + min Variable
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # 額外維護一個紀錄當前最小值的變數
        curr_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Diff
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)  # 第一個元素的差值 = 0
            self.min_val = val
        else:
            diff = val - self.min_val
            self.stack.append(diff)
            if diff < 0:
                self.min_val = val  # 更新最小值

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            # 當前最小值是被更新的那個，要回復舊的 min
            self.min_val -= diff

    def top(self) -> int:
        diff = self.stack[-1]
        if diff >= 0:
            return self.min_val + diff
        else:
            return self.min_val  # 這層是新的最小值

    def getMin(self) -> int:
        return self.min_val
