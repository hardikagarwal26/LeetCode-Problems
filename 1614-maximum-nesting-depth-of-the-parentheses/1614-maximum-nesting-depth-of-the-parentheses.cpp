class Solution {
public:
    int maxDepth(string s) {
        int ans=0 , p=0;
        for(char c:s)
        {
            if(c == '(')
            {
                p++;
                ans = max(ans,p);
            }
            else if(c == ')')
                p--;
        }
        return ans;
    }
};