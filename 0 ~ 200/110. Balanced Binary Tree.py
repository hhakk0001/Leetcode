"""251007"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# FT: Recursion(Top-down)
def isBalanced(self, root: TreeNode) -> bool:
    if root is None:
        return True

    left_height = self.get_height(root.left)
    right_height = self.get_height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return self.isBalanced(root.left) and self.isBalanced(root.right)


def get_height(self, node: TreeNode) -> int:
    if node is None:
        return 0
    else:
        return 1 + max(self.get_height(node.left), self.get_height(node.right))


# Recursion: Bottom-up
def isBalanced(self, root: TreeNode) -> bool:
    return self.check(root) != -1


def check(self, node: TreeNode) -> int:
    # 空節點高度為 0
    if not node:
        return 0

    # 檢查左子樹
    left_height = self.check(node.left)
    if left_height == -1:
        return -1  # 若左子樹不平衡，直接返回

    # 檢查右子樹
    right_height = self.check(node.right)
    if right_height == -1:
        return -1  # 若右子樹不平衡，直接返回

    # 若高度差大於 1，也是不平衡
    if abs(left_height - right_height) > 1:
        return -1

    # 若平衡，回傳當前節點高度
    return max(left_height, right_height) + 1
