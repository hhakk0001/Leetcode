"""251002"""


# FT
def longestPalindrome(self, s: str) -> int:
    letters = dict()
    length = 0
    is_odd = False

    for char in s:
        letters[char] = letters.get(char, 0) + 1

    for val in letters.values():
        if val % 2 == 0:
            length += val
        else:
            is_odd = True
            if val >= 3:
                length += val - 1

    if is_odd:
        length += 1

    return length


# FT: improved
def longestPalindrome(self, s: str) -> int:
    letters = dict()
    length = 0
    has_odd = False

    for char in s:
        letters[char] = letters.get(char, 0) + 1

    for val in letters.values():
        length += (val // 2) * 2  # 加上最大偶數部分
        if val % 2 == 1:  # 紀錄是否有奇數
            has_odd = True

    # 如果有字母出現奇數次，長度加一(中心的奇數字母)
    if has_odd:
        length += 1

    return length


# Greedy Way (Optimized)
def longestPalindrome(self, s: str) -> int:
    odd_freq_chars_count = 0
    frequency_map = {}

    for c in s:
        # 更新當前字母的出現次數
        frequency_map[c] = frequency_map.get(c, 0) + 1

        # 更新當前出現次數為奇數的字母數量
        if frequency_map[c] % 2 == 1:
            odd_freq_chars_count += 1
        else:
            odd_freq_chars_count -= 1

    # 如果有字母出現奇數次，減去出現奇數次字母的數量並加一(中心的奇數字母)。
    if odd_freq_chars_count > 0:
        return len(s) - odd_freq_chars_count + 1
    else:
        return len(s)


# Greedy Way (Hash Set)
def longestPalindrome(self, s: str) -> int:
    character_set = set()
    res = 0

    for c in s:
        # 如果集合包含當前字母
        if c in character_set:
            character_set.remove(c)
            # 把兩個字母算入總長度內
            res += 2
        else:
            # Add the character to the set
            character_set.add(c)

    # 如果有字母出現奇數次，長度加一(中心的奇數字母)。
    if character_set:
        res += 1

    return res
