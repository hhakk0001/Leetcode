"""251126"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# FT: Recursive
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def preorderTraverse(root):
        if root == None:
            return

        res.append(root.val)
        preorderTraverse(root.left)
        preorderTraverse(root.right)

    preorderTraverse(root)
    return res


# Iterative
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    if root == None:
        return res

    # 利用堆疊的特性進行走訪
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)

        # 堆疊是後進先出，所以先 push 右子點
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return res


# Morris preorder traversal
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    if root == None:
        return res

    cur = root
    while cur:
        # 如果 cur 沒有左子樹，就不必建立引線
        if cur.left is None:
            res.append(cur.val)
            cur = cur.right
        else:
            # 找中序時 cur 的 predecessor
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right

            if pre.right is None:
                res.append(cur.val)  # 拜訪點在這裡（前序特性）
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                cur = cur.right

    return res
