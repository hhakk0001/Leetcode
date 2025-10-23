from collections import defaultdict

"""251023"""


# FT: TLE
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagrams = []

    for s in strs:
        if anagrams:
            has_group = False

            for group in anagrams:
                if sorted(group[0]) == sorted(s):
                    group.append(s)
                    has_group = True
                    break

            if not has_group:
                anagrams.append([s])
        else:
            anagrams.append([s])

    return anagrams


# sorted string as key
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    groups = {}

    for s in strs:
        key = "".join(sorted(s))  # 排序後作為 canonical form
        # 如果用 defaultdict 就不用檢查空 key
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return list(groups.values())


# array count as key
def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    # 使用 defaultdict 方便自動建立 list
    groups = defaultdict(list)

    for s in strs:
        # 建立 26 維計數陣列（僅適用小寫 a-z）
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1

        # 將 list 轉成 tuple（不可變，可作為 dict key）
        key = tuple(count)

        # 依 key 分組
        groups[key].append(s)

    # 回傳所有分組結果
    return list(groups.values())
