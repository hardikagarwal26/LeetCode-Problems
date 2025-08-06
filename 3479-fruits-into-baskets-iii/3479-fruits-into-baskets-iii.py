class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        rem = 0
        n = len(baskets)

        for fruit in fruits:
            placed = False

            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    placed = True
                    break

            if not placed:
                rem += 1

        return rem