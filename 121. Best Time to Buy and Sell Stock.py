'''250904'''

# Brute force: 超時
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
        
    return max_profit

# One-pass DP
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
    
    return max_profit


