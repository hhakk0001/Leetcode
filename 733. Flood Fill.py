"""251106"""

from typing import List
from collections import deque


# FT: DFS
def floodFill(
    self, image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:
    # get length and width of image
    m, n = len(image), len(image[0])
    old_color = image[sr][sc]

    def dfs_fill(r, c):
        # check if the pixel meet the condition
        if not (0 <= r < m and 0 <= c < n) or image[r][c] != old_color:
            return

        image[r][c] = color

        # recursive call for four directions
        dir_set = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
        for nr, nc in dir_set:
            dfs_fill(nr, nc)

    if old_color != color:
        dfs_fill(sr, sc)

    return image


# DFS: modified
def floodFill(
    self, image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:
    # Get the dimensions of the image
    m, n = len(image), len(image[0])

    # Store the original color of the starting pixel
    old_color = image[sr][sc]
    if old_color == color:
        return image

    # Define 4-directional movements
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Recursive DFS function
    def dfs(r, c):
        # Check boundaries and the color
        if not (0 <= r < m and 0 <= c < n) or image[r][c] != old_color:
            return

        image[r][c] = color

        # Recursively fill the 4 adjacent pixels
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    dfs(sr, sc)

    return image


# BFS
def floodFill(
    self, image: List[List[int]], sr: int, sc: int, color: int
) -> List[List[int]]:
    m, n = len(image), len(image[0])
    old_color = image[sr][sc]

    # If the old color is the same as the new color, nothing to change
    if old_color == color:
        return image

    # Initialize BFS queue and directions
    queue = deque([(sr, sc)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Start BFS
    while queue:
        r, c = queue.popleft()
        image[r][c] = color  # Fill with new color

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Check bounds and whether the color matches
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == old_color:
                queue.append((nr, nc))

    return image
