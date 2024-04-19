class Solution {
public:
    void dfs(vector<vector<char>> &m,int x, int y, int r, int c){
        if(x<0||y<0||x>=r||y>=c||m[x][y]!='1'){
            return;
        }
        m[x][y]='2';
        dfs(m,x+1,y,r,c);
        dfs(m,x,y+1,r,c);
        dfs(m,x-1,y,r,c);
        dfs(m,x,y-1,r,c);
    }
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        if(rows==0){
            return 0;
        }
        int cols = grid[0].size();
        int cnt = 0;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]=='1'){
                    dfs(grid,i,j,rows,cols);
                    cnt++;
                }
            }
        }
        return cnt;
    }
};