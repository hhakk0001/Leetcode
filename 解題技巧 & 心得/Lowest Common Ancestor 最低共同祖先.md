# Lowest Common Ancestor 最低共同祖先

又稱最近共通祖先。

## 定義

> “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).” 

在維基百科上，LCA 的定義是指在樹或 DAG 結構中，對於 `p, q` 兩個節點，有一個最低的節點 T 滿足:
1. 同時為 `p, q` 的祖先 (包含 p 或 q 自身)。
2. 在樹 (圖) 為中最深 / 離 `p, q` 最近的節點。

經典題型有: Leetcode 235/236。

### 解法: 分類討論

以 Leetcode 236 為例，若目前給定一個二元搜尋樹 root = [6,2,8,0,4,7,9,null,null,3,5]:
![alt text](LCA-1.png)

我們可以將走訪結果分成下列幾種情況討論:
1. 當前為空節點: 沒有子樹或空樹，**返回當前(空)節點**。
2. 當前為 `p` 或 `q` 節點: 此時若另一個節點在當前節點的子樹中，那麼 LCA 只有可能是當前節點(或以上); 如果不在，也就不需要繼續往下遞迴搜尋。因此，**返回當前節點**。
1. 其他:
   1. `p、q` 分別在左右子樹: 只有可能是當前節點，**返回當前節點**。
   2. `p、q` 都在左/右子樹: **返回遞迴該子樹的結果**。 
   3. 都不在: 兩節點不在當前子樹中，**返回空節點**。



