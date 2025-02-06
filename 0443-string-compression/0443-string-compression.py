class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        index = 0
        while i<n:
            curr = chars[i]
            cnt =  0
            while i<n and  chars[i] == curr:
                i+=1
                cnt+=1
            chars[index] = curr
            index+=1
            if cnt>1:
                for ch in str(cnt):
                    chars[index] = ch
                    index+=1
        return index

        