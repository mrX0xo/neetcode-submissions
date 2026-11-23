class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rank = list()


        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                if prices[sell] - prices[buy] >= 1:
                    rank.append(prices[sell] - prices[buy])
        
        rank.sort(reverse=True)

        if rank == []:
            return 0
        else:    
            return rank[0]
         

        