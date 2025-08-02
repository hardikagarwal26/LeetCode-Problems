class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        numbermap = {}
        minVal = float("inf")
        
        for x,y in zip(basket1 , basket2):
            numbermap[x] = numbermap.get(x,0) + 1
            numbermap[y] = numbermap.get(y,0) - 1
            minVal = min(minVal , x , y)
        
        transfer = []
        for value , balance in (numbermap.items()):
            if balance & 1 :
                return -1
            transfer.extend([value]*(abs(balance)//2))

        transfer.sort()
        cost = 0
        m = len(transfer)
        for i in range(m//2):
            cost += min(transfer[i] , 2*minVal)
        return cost
        