class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for n in range(n+1 , 10**7):
            map = Counter(str(n))
            if all(k == str(v) for k , v in map.items()) : return n

        