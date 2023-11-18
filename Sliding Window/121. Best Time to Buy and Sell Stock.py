
# Wrong Answer 144 / 212 testcases passed

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lo = 0

        hi = len(prices) - 1

        stock = dict()
        stock["max"] = {"index": 10_000, "value": 0}
        stock["min"] = {"index": -1, "value": 10_000}

        while lo < hi:
            hi_price = prices[hi]
            lo_price = prices[lo]

            if hi_price > stock["max"]["value"]:

                stock["max"]["index"] = hi
                stock["max"]["value"] = hi_price

                if prices[hi-1] < stock["min"]["value"] \
                and (hi-1) < stock["max"]["index"] \
                and (hi-1) > hi:
                    stock["min"]["index"] = hi-1
                    stock["min"]["value"] = prices[hi-1]  

            
            if lo_price < stock["min"]["value"]:

                stock["min"]["index"] = lo
                stock["min"]["value"] = lo_price

                if prices[lo+1] > stock["max"]["value"] \
                    and (lo+1) > stock["min"]["index"] \
                    and (lo+1) < hi:

                    stock["max"]["index"] = lo+1
                    stock["max"]["value"] = prices[lo+1]
            
            hi -= 1
            lo += 1            
        
        result = stock["max"]["value"] - stock["min"]["value"]
        return result if result>0 else 0




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 10_000

        max_profit = 0

        for i in prices:
            
            profit = i - min

            if profit>max_profit:
                max_profit = profit
            if i < min:
                min = i
        return max_profit
            

# Kendi sentezlediğim çözüm 1            
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        min_price = 10_000

        for price in prices:
            min_price = min(price, min_price)
            local_profit = price - min_price
            profit = max(profit, local_profit)

        return profit if profit > 0 else 0




