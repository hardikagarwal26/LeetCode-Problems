class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        sub_xor = [0]*n
        family = [set() for _ in range(n)]
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs_xor(index , parent):
            sub_xor[index] = nums[index]
            family[index].add(index)
            
            for neighbor in graph[index]:
                if neighbor != parent:
                    dfs_xor(neighbor , index)
                    sub_xor[index] ^= sub_xor[neighbor]
                    family[index].update(family[neighbor])

        dfs_xor(0,-1)
        total_xor = sub_xor[0]
        res = math.inf

        for i in range(1,n):
            for j in range(i+1,n):
                xi = sub_xor[i]
                xj = sub_xor[j]

                if j in family[i]:
                    f = xj
                    s = xi^xj
                    t = total_xor ^ xi
                elif i in family[j]:
                    f = xi
                    s = xj ^ xi
                    t = total_xor ^ xj
                else:
                    f = xi
                    s = xj
                    t = total_xor ^ xi ^ xj
                res = min(res,max(f,s,t)-min(f,s,t))
        return res
