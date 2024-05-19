class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n =grid.size();
        int m = grid[0].size();
        int total=0, count=0;
        queue<pair<int,int>> q;
        for(int i =0 ; i<n; i++)
        {
            for(int j=0;j<m;j++)
            {
                if(grid[i][j]==2)
                q.push({i,j});
                if(grid[i][j]!=0)
                total++;
            }
        }
        int x[4]={0,0,1,-1};
        int y[4]={1,-1,0,0};
        int ans=0;
        while(!q.empty())
        {
            int s = q.size();
            count+=s;
            while(s--)
            {
                int c = q.front().second , d = q.front().first;
                q.pop();
                for(int i = 0 ;i<4;i++)
                {
                    int nc=d+x[i] , nd=c+y[i];
                    if(nc<0 || nd<0 || nc>=n || nd>=m || grid[nc][nd]!=1)
                    continue;
                    grid[nc][nd]=2;
                    q.push({nc,nd});
                }
            }
            if(!q.empty())
                ans++;
        }
        if(total==count)
            return ans;
        return -1;
    }
};