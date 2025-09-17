"""250917"""


# 雙指標
def addBinary(self, a: str, b: str) -> str:
    a_ptr, b_ptr = len(a) - 1, len(b) - 1
    res = []
    carry = 0

    while a_ptr >= 0 or b_ptr >= 0 or carry == 1:
        digit_a = a[a_ptr] if a_ptr >= 0 else "0"
        digit_b = b[b_ptr] if b_ptr >= 0 else "0"

        total = int(digit_a) + int(digit_b) + carry
        res.append(str(total % 2))
        carry = total // 2

        a_ptr -= 1
        b_ptr -= 1

    return "".join(reversed(res))


# Python 內建解法
def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
