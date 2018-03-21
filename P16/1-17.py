class Solution(object):
    def coinChange(self, coins, amount):
        coins=list[1,2,5,10,20,50,100]
        amount=342
        dp = [0] + [-1] * amount
        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]
    print dp[amount]
