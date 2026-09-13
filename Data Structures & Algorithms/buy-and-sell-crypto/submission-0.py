class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for left in range(0, len(prices)):
            for right in range(left, len(prices)):
                if (prices[right] - prices[left]) > res:
                    res = prices[right] - prices[left]
        
        return res