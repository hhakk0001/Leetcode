from collections import deque  # for BFS

"""251005"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# FT: Recursion
def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        self.invertTree(root.left)
        self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp

    return root


# Recursion: improved
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None

    # 交換
    root.left, root.right = root.right, root.left
    # 遞迴翻轉子樹
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root


# Iteration: BFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


# Iteration: DFS
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None

    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root
