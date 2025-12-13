"""251203"""


# FT: Sliding Window
def maxVowels(self, s: str, k: int) -> int:
    max_vowels = 0
    curr_vowels = 0

    for i in range(k):
        if s[i] in "aeiou":
            curr_vowels += 1

    max_vowels = curr_vowels

    for i in range(k, len(s)):
        if s[i - k] in "aeiou":
            curr_vowels -= 1
        if s[i] in "aeiou":
            curr_vowels += 1
        max_vowels = max(max_vowels, curr_vowels)
        if max_vowels == k:
            return k

    return max_vowels


# BF
def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiou")
    max_count = 0
    n = len(s)

    for i in range(n - k + 1):
        count = 0
        # 檢查從 i 開始長度為 k 的子字串
        for j in range(i, i + k):
            if s[j] in vowels:
                count += 1
        max_count = max(max_count, count)

    return max_count
