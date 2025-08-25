class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row , col = len(mat) , len(mat[0])
        ans = []
        cr , cl = 0 , 0
        up = True
        
        while len(ans) != row*col:
            if up:
                while cr >= 0 and cl < col:
                    ans.append(mat[cr][cl])

                    cr -= 1
                    cl += 1
                if cl == col:
                    cl -= 1
                    cr += 2
                else:
                    cr += 1
                up = False
            else:
                while cl >= 0 and cr < row:
                    ans.append(mat[cr][cl])

                    cl -= 1
                    cr += 1
                if cr == row:
                    cr -= 1
                    cl += 2
                else:
                    cl += 1
                up = True
        return ans
