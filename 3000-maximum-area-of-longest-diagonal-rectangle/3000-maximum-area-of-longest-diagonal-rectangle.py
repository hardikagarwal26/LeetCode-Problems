class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = 0
        maxd = 0
        for l ,w in dimensions:
            diag = math.sqrt(l*l + w*w)
            if diag > maxd:
                area = l*w
                maxd = diag
            elif diag == maxd:
                area = max(area , l*w)
        return area
        