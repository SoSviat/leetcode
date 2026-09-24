class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        
        res = []

        for i in range(len(prices)):
            sale = prices[i]

            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    sale = prices[i] - prices[j]
                    break

            res.append(sale)
            
        return res