"""250915"""


# First Try: Two pointers
def isPalindrome(self, s: str) -> bool:
    s_new = ""

    for char in s:
        if char.isalpha() or char.isdigit():
            s_new += char

    s_new = s_new.lower()
    left_ptr = 0
    right_ptr = len(s_new) - 1

    while left_ptr <= right_ptr:
        if s_new[left_ptr] != s_new[right_ptr]:
            print(left_ptr, right_ptr)
            return False
        left_ptr += 1
        right_ptr -= 1

    return True


# 修正-1
def isPalindrome(self, s: str) -> bool:
    clean_char = [char.lower() for char in s if char.isalnum()]
    left_ptr, right_ptr = 0, len(clean_char) - 1

    while left_ptr <= right_ptr:
        if clean_char[left_ptr] != clean_char[right_ptr]:
            return False
        left_ptr += 1
        right_ptr -= 1

    return True


# 修正-2
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


# 暴力法
def isPalindrome(s: str) -> bool:
    clean = [c.lower() for c in s if c.isalnum()]
    return clean == clean[::-1]
