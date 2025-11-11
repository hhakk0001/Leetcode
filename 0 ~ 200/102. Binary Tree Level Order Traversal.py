"""251110"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# FT: BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty
        if root is None:
            return []

        # Initialize queue for BFS
        queue = deque()
        queue.append(root)

        # Result of level order traversal
        res = []

        # Loop until there are no more nodes to process
        while queue:
            # hold values of nodes at current level
            cur_level_nodes = []

            # Number of nodes at current level
            num_of_nodes = len(queue)

            # Process all nodes at the current level
            for _ in range(num_of_nodes):
                cur_node = queue.popleft()
                cur_level_nodes.append(cur_node.val)

                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)

            # Add current level's result to final output
            res.append(cur_level_nodes)

        return res
