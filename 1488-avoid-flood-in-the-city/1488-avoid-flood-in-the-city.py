class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [1] * n
        map = {}
        sl = SortedList()

        for i , x in enumerate(rains):
            if x == 0: sl.add(i)
            else:
                res[i] = -1
                if x in map:
                    bs = sl.bisect_left(map[x])
                    if bs == len(sl) : return []
                    res[sl[bs]] = x
                    sl.discard(sl[bs])
                map[x] = i
        return res
        