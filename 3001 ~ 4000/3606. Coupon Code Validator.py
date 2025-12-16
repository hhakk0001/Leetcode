"""251213"""

from typing import List


# Method 1
def validateCoupons(
    self, code: List[str], businessLine: List[str], isActive: List[bool]
) -> List[str]:
    categories = ("electronics", "grocery", "pharmacy", "restaurant")
    e, g, p, r = [], [], [], []

    for i in range(len(code)):
        if not code[i] or not all(ch.isalnum() or ch == "_" for ch in code[i]):
            continue

        if businessLine[i] not in categories:
            continue

        if not isActive[i]:
            continue

        if businessLine[i].startswith("e"):
            e.append(code[i])
        if businessLine[i].startswith("g"):
            g.append(code[i])
        if businessLine[i].startswith("p"):
            p.append(code[i])
        if businessLine[i].startswith("r"):
            r.append(code[i])

    return sorted(e) + sorted(g) + sorted(p) + sorted(r)


# Modified-1
def validateCoupons(
    self, code: List[str], businessLine: List[str], isActive: List[bool]
) -> List[str]:
    allowed = {"electronics", "grocery", "pharmacy", "restaurant"}
    categorized = {
        "electronics": [],
        "grocery": [],
        "pharmacy": [],
        "restaurant": [],
    }

    for i in range(len(code)):
        c = code[i]
        b = businessLine[i]
        a = isActive[i]

        if not c:
            continue
        if not all(ch.isalnum() or ch == "_" for ch in c):
            continue
        if b not in allowed or not a:
            continue

        categorized[b].append(c)

    result = []
    for cat in ["electronics", "grocery", "pharmacy", "restaurant"]:
        result.extend(sorted(categorized[cat]))
    return result


# Modified-2
def validateCoupons(
    self, code: List[str], businessLine: List[str], isActive: List[bool]
) -> List[str]:
    BUSINESS_LINE_TO_CATEGORY = {
        "electronics": 0,
        "grocery": 1,
        "pharmacy": 2,
        "restaurant": 3,
    }
    groups = [[] for _ in range(len(BUSINESS_LINE_TO_CATEGORY))]

    for s, bus, active in zip(code, businessLine, isActive):
        category = BUSINESS_LINE_TO_CATEGORY.get(bus, -1)
        if s and category >= 0 and active and all(c == "_" or c.isalnum() for c in s):
            groups[category].append(s)

    ans = []
    for g in groups:
        g.sort()
        ans += g
    return ans
