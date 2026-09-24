class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:

        res = list(prices)
        stack = []

        for i in range(len(prices)):
            
            while stack and prices[i] <= prices[stack[-1]]:
                index = stack.pop()
                res[index] = prices[index] - prices[i]
                
            stack.append(i)

        return res


        
        # res = []

        # for i in range(len(prices)):
        #     sale = prices[i]

        #     for j in range(i+1,len(prices)):
        #         if prices[i] >= prices[j]:
        #             sale = prices[i] - prices[j]
        #             break

        #     res.append(sale)
            
        # return res
        # O(n2)
        # O(n)