# Leetcode
Leetcode 的練習紀錄


## 重要題型

以下紀錄一些可以多刷，或作為基礎來解其他進階題型的題目。

- [Leetcode](#leetcode)
  - [重要題型](#重要題型)
    - [基礎](#基礎)
    - [二元樹](#二元樹)
    - [SQL/Pandas](#sqlpandas)
    - [數學/數論相關](#數學數論相關)
    - [雙指標 (Two Pointers)](#雙指標-two-pointers)
    - [滑動窗口 (Sliding Window)](#滑動窗口-sliding-window)
    - [位元運算 (Bitwise Operation)](#位元運算-bitwise-operation)
- [貪心法 (Greedy)](#貪心法-greedy)
  - [參考刷題順序](#參考刷題順序)


### 基礎

無太多 DS & Algo 的題目，可能包含簡單數學概念
適合開始正式刷題前用來適應開發環境及熟悉語法。

* 1512. Number of Good Pairs: 排列組合的應用，可將暴力法降到線性時間。
* 709. To Lower Case: 了解 ASCII 的概念，並熟悉各語言自帶的大小寫轉換函式
* 231. Power of Two: 位運算，以及判斷是否為題目極限值的因數
* 867. Transpose Matrix: 矩陣運算，然後 numpy 有直接轉至的函式。
* 1422. Maximum Score After Splitting a String: 利用前綴和的方式減少一層迴圈。
* 852. Peak Index in a Mountain Array: 二分搜尋的變體，注意邊界的更新。

### 二元樹

基礎:
* 走訪:
  * [144. 二元樹前序走訪](/0%20~%20200/144.%20Binary%20Tree%20Preorder%20Traversal.md)
* 求最低公共祖先(Lowest Common Ancestor, LCA):
  * [236.](/201%20~%20400/236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree.md) / [235.](/201%20~%20400/235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree.md)

### SQL/Pandas

* 584. Find Customer Referee: 注意 Null 處理與 `<>` 的使用
* 1757. Recyclable and Low Fat Products: `=`

### 數學/數論相關

參考: [數論相關原理](/解題技巧%20&%20心得/數論相關原理.md)

* 258. Add Digits: 考數根(digital root) 和模運算。
  * [最優解的一種易懂說明](https://leetcode.cn/problems/add-digits/solutions/1301157/ge-wei-xiang-jia-by-leetcode-solution-u4kj/comments/2467095/)
* 奇偶性: 
  * [1523.](1523.%20Count%20Odd%20Numbers%20in%20an%20Interval%20Range.md)


### 雙指標 (Two Pointers)

* 相向雙指標: 指標從兩端開始向中間移動
  * 基礎: [167. Two Sum II](/0%20~%201000/0%20~%20200/167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.md) / [15. 3Sum](/0%20~%201000/0%20~%20200/15.%203Sum.md) / [11. Container With Most Water](/0%20~%201000/0%20~%20200/11.%20Container%20With%20Most%20Water.md)
  * 進階: [42. Trapping Rain Water](/0%20~%201000/0%20~%20200/42.%20Trapping%20Rain%20Water.md)

### 滑動窗口 (Sliding Window)

參考: [Sliding Window](/解題技巧%20&%20心得/Sliding%20Window%20滑動視窗.md)

* 固定長度
  * 基礎題型: [1456.](1456.%20Maximum%20Number%20of%20Vowels%20in%20a%20Substring%20of%20Given%20Length.md) / [643.](643.%20Maximum%20Average%20Subarray%20I.md) / [1343.](/1001%20~%202000/1343.%20Number%20of%20Sub-arrays%20of%20Size%20K%20and%20Average%20Greater%20than%20or%20Equal%20to%20Threshold.md)
* 不固定長度
  * 求最長/最大:
  * 求最短/最小:

### 位元運算 (Bitwise Operation)

參考: [集合論到位元運算](/解題技巧%20&%20心得/應用集合於位運算.md)
* 基礎
  * [3370.](3370.%20Smallest%20Number%20With%20All%20Set%20Bits.md) / [3226.](3226.%20Number%20of%20Bit%20Changes%20to%20Make%20Two%20Integers%20Equal.md)

# 貪心法 (Greedy)

* 從最左(右)開始貪心: 可思考與線性/狀態機 DP 之不同處
  * [955.](/0%20~%201000/801%20~%201000/955.%20Delete%20Columns%20to%20Make%20Sorted%20II.md)


## 參考刷題順序

* [灵茶山艾府-如何科学刷题？](https://leetcode.cn/discuss/post/3141566/)
* [Neetcode 150](https://neetcode.io/roadmap)