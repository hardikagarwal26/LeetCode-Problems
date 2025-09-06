class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for l,r in queries:
            temp = 0
            st = 1
            end = 4
            for i in range(1,16):
                left = max(l,st)
                right = min(r,end-1)
                if right >= left:
                    temp = temp + (right-left+1)*i
                st *= 4
                end *= 4
            ans = ans + ceil(temp/2)
        return ans
        