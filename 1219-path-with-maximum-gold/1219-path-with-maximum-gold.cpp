class Solution {
private:
    int maxi=0;

    void dfs(int row,int col,int n,int m,vector<vector<int>>&grid,int sum){
        int delr[]={1,0,-1,0};
        int delc[]={0,-1,0,1};

        for(int i=0;i<4;i++){
            int nrow=row+delr[i];
            int ncol=col+delc[i];

            if(nrow>=0 && nrow<n && ncol>=0 && ncol<m && grid[nrow][ncol]!=0){
                int temp=grid[nrow][ncol];
                sum+=temp;
                grid[nrow][ncol]=0;
               
                maxi=max(maxi,sum);
                dfs(nrow,ncol,n,m,grid,sum);
               
                sum-=temp;
                grid[nrow][ncol]=temp;
            }
        }
    }
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        int n=grid.size();
        int m=grid[0].size();
        int sum=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                dfs(i,j,n,m,grid,sum);
        return maxi;
            
    }
};