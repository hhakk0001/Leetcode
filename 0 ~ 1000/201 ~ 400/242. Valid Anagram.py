"""250929"""


# FT: Hash Table
def isAnagram(self, s: str, t: str) -> bool:
    letters = dict()

    for char in s:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    for char in t:
        if char in letters and letters[char] > 0:
            letters[char] -= 1
        else:
            return False

    for k, v in letters.items():
        if v != 0:
            return False

    return True


# Hash Table: 修正版
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):  # 長度不同，直接返回 False
        return False

    letters = dict()

    # 等效但更簡約的寫法
    for char in s:
        letters[char] = letters.get(char, 0) + 1

    for char in t:
        if char not in letters or letters[char] == 0:
            return False
        letters[char] -= 1

    return True  # 不需要再檢查字典，因為長度已保證相等


# Array Count
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):  # 長度不同，直接返回 False
        return False

    count = [0] * 26  # a-z 共 26 個字母

    for ch in s:
        count[ord(ch) - ord("a")] += 1

    for ch in t:
        count[ord(ch) - ord("a")] -= 1
        if count[ord(ch) - ord("a")] < 0:
            return False

    return True


# Sorting
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
