class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ans.append(n)
            while len(ans) >= 2:
                n1 , n2 = ans[-2] , ans[-1]
                g = gcd(n1,n2)
                if g == 1: break
                ans.pop()
                ans[-1] = n1 * n2 // g
        return ans

        