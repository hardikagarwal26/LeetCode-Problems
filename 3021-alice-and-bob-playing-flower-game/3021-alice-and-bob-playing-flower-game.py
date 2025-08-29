class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        oddN = (n+1) // 2
        evenN = n //2

        oddM = (m+1)//2
        evenM = m // 2

        return oddN * evenM + evenN * oddM
        