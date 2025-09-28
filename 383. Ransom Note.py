"""250928"""


# FT: Hash Table
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    letters = dict()

    # 記錄 magazine 中每個字母的出現次數
    for char in magazine:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    # 檢查 ransomNote 中的每個字母是否存在且數量足夠
    for char in ransomNote:
        if char in letters and letters[char] > 0:
            letters[char] -= 1
        else:
            return False

    return True
