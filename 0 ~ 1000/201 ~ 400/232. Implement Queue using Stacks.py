"""250914"""


# First Try:
class MyQueue:
    def __init__(self):
        self._stack_1 = []
        self._stack_2 = []

    def push(self, x: int) -> None:
        self._stack_1.append(x)

    def pop(self) -> int:
        while self._stack_1:
            self._stack_2.append(self._stack_1.pop())
        res = self._stack_2.pop()
        while self._stack_2:
            self._stack_1.append(self._stack_2.pop())

        return res

    def peek(self) -> int:
        while self._stack_1:
            self._stack_2.append(self._stack_1.pop())
        res = self._stack_2.pop()
        self._stack_2.append(res)
        while self._stack_2:
            self._stack_1.append(self._stack_2.pop())

        return res

    def empty(self) -> bool:
        return len(self._stack_1) == 0


# 修改
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()  # Ensure output stack has the current front
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:  # Transfer elements if output stack is empty
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output
