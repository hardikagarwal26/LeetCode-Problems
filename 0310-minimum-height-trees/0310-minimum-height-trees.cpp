class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(n==1)
        return {0};
        vector<int> ans;
        queue<int> q;
        vector<vector<int>> g(n);
        vector<int> count(n,0);
        for(vector<int> edge:edges)
        {
            count[edge[0]]++;
            count[edge[1]]++;
            g[edge[0]].push_back(edge[1]);
            g[edge[1]].push_back(edge[0]);
        }
        for(int i=0;i<n;i++)
        {
            if(count[i]==1)
            q.push(i);
        }
        while(n>2)
        {
            int size=q.size();
            n=n-size;
            while(size--)
            {
                int node = q.front();
                q.pop();
                for(int adj:g[node])
                {
                    count[adj]--;
                    if(count[adj]==1)
                    q.push(adj);
                }
            }
            size--;
        }
        while(!q.empty())
        {
            int node = q.front();
            q.pop();
            ans.push_back(node);
        }
        return ans;
    }
};