# Binary Search 二分搜尋

二分搜尋本身的概念不難，但可以有非常多的變化。
以下實作程式以**閉區間**為主。

## 找一個特定目標值

最基礎的版本，搜尋一個具有特定值的元素，  
* 若該元素存在，回傳其索引。
* 若該元素不存在，回傳 -1。

> 例 1:  
> `nums = [1, 3, 5, 7]`, `target = 5`  
> left = 0, right = 3, mid = 1, `nums[1] < target`  
> left = 2, right = 3 mid = 2, `nums[2] == target`  
> end loop and `return mid`
>
> 例 2:  
> `nums = [1, 3, 5, 7]`, `target = 4`  
> left = 0, right = 3, mid = 1, `nums[1] < target`  
> left = 2, right = 3, mid = 2, `nums[2] > target`  
> left = 2, right = 1, end loop and `return -1`

```python
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        # 該寫法是避免某些程式語言出現溢位問題
        # Python 可以直接寫 m = (i + j) // 2
        mid = left + (right - left) // 2  # 計算中點索引 m

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    return -1  # 未找到目標元素，返回 -1
```

## 找一個特定目標值的插入位置

考慮前面的程式碼，當陣列中不存在 `target`，
* `left` 最終會落在 **第一個大於 `target` 的元素** 上
* `right` 最終會落在 **最後一個小於 `target` 的元素** 上

該情況可以分為兩種情形討論:

### 無重複值: 找左指標

由於陣列的開頭地址是固定的，插入元素時通常會選擇將元素向後移。  
因此，將原本回傳 -1 的情況改為 `left` 即可。

> `nums = [1, 3, 5, 7]`, `target = 4`  
> left = 0, right = 3, mid = 1, `nums[1] < target`  
> left = 2, right = 3, mid = 2, `nums[2] > target`  
> left = 2, right = 1, end loop and `return left`

```py
def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
```

### 有重複值: 依題目條件找左右邊界

考慮 `target` 可能不只一個的情況，
插入位置則根據要求選擇值皆為 `target` 的子陣列之邊界，  
若未特別提及則通常是左邊界，理由同前面所述。

以左邊界來說，此時目標是找到位於 **最左** 且 **值為 target** 的元素，  
因此當出現 `nums[mid] == target` 的情況，  
就改為繼續向左半區縮減，即執行 `right = mid - 1`。  

這樣當左指標超過右指標時，  
`left` 所在的位置就會是 **第一個(大於)等於 target 的元素**。


> `nums = [1, 2, 3, 3, 5, 5, 5, 7]`, `target = 3`  
> left = 0, right = 7, mid = 3, `nums[3] == target`  
> left = 0, right = 2, mid = 1, `nums[1] < target`  
> left = 2, right = 2, mid = 2, `nums[2] == target`  
> left = 2, right = 1, end loop and `return left`

```py
def left_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] >= target:
            right = mid - 1

    # 若作為子函式，此判斷可挪至主程式中
    if left < 0 or left >= len(nums):
        return -1

    return left if nums[left] == target else -1
```

---

右邊界也是類似的處理方式，只是左右相反。

> `nums = [1, 2, 3, 3, 5, 5, 5, 7]`, `target = 5`  
> left = 0, right = 7, mid = 3, `nums[3] < target`  
> left = 4, right = 7, mid = 5, `nums[5] == target`  
> left = 6, right = 7, mid = 6, `nums[6] == target`  
> left = 8, right = 7, end loop and `return right`


```py
def right_bound(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    # 若作為子函式，此判斷可挪至主程式中
    if right < 0 or right >= len(nums):
        return -1

    return right if nums[right] == target else -1
```

注意: 若 **`target` 不存在**
* **左邊界**返回的是**大於 `target` 的第一個元素**。
* **右邊界**返回的是**小於 `target` 的最後一個元素**。