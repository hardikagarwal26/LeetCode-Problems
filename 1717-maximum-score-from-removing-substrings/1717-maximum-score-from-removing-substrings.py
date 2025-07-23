class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x<y:
            return self.solve(s,'b','a',y,x)
        else:
            return self.solve(s,'a','b',x,y)
    
    def solve(self , s:str , fr:str , sec:str , fp:int , sp:int):
        score = 0
        stack = []
        for ch in s:
            if stack and stack[-1] == fr and ch == sec:
                stack.pop()
                score += fp
            else:
                stack.append(ch)
        final_stack = []
        for ch in stack:
            if final_stack and final_stack[-1] == sec and ch == fr:
                final_stack.pop()
                score += sp
            else:
                final_stack.append(ch)
        return score
            
        