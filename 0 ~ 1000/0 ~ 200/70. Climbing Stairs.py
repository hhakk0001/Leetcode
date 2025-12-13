"""251003"""


# FT: Recursion, but TLE
def climbStairs(self, n: int) -> int:
    if n > 2:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    else:
        return n


# FT: Iteration + DP (Tabulation)
def climbStairs(self, n: int) -> int:
    climb_ways = [0] * (n + 1)
    climb_ways[0], climb_ways[1] = 1, 1

    for stair in range(2, n + 1):
        climb_ways[stair] = climb_ways[stair - 1] + climb_ways[stair - 2]

    return climb_ways[n]


# Recursion + Memoization
def climbStairs(self, n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
    return memo[n]


# Space Optimization: rolling variable
def climbStairs(self, n: int) -> int:
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
