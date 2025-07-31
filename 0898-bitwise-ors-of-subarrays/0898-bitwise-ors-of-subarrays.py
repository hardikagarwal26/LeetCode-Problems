class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        previous = set()
        for i in arr:
            current = {i}
            for j in previous:
                current.add(j | i)
            result.update(current)
            previous = current
        return len(result)

        