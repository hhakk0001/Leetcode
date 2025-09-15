import timeit

# 測試資料
n = 10000
lst = [str(i) for i in range(n)]


# 測試 1: 使用 +
def test_plus():
    s = ""
    for i in lst:
        s = s + i
    return s


# 測試 2: 使用 +=
def test_plus_equal():
    s = ""
    for i in lst:
        s += i
    return s


# 測試 3: 使用 join
def test_join():
    return "".join(lst)


# 使用 timeit 測試每個方法的耗時
time_plus = timeit.timeit(test_plus, number=1)
time_plus_equal = timeit.timeit(test_plus_equal, number=1)
time_join = timeit.timeit(test_join, number=1)

print(time_plus, time_plus_equal, time_join)
