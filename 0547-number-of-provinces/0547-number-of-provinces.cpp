class Solution {
public:
    void dfs(vector<vector<int>>& isConnected, int i , vector<bool> &visited)
    {
        visited[i]=true;
        for(int j = 0 ; j<isConnected.size(); j++)
        {
            if(isConnected[i][j]==1 && visited[j]==false)
            {
                dfs(isConnected,j,visited);
            }
        }
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int ans=0;
        vector<bool> visited(isConnected.size() , false);
        for(int i=0 ; i<isConnected.size() ; i++)
        {
            if(visited[i]==false)
            {
                dfs(isConnected,i,visited);
                ans++;
            }
        }
        return ans;
    }
};