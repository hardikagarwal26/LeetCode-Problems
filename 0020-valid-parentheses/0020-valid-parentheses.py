class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {')':'(' , '}' : '{' , ']':'['}
        for i in s:
            if i in hash:
                if stack and stack[-1] == hash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
        