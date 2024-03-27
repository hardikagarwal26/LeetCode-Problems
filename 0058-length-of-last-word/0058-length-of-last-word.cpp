class Solution {
public:
    int lengthOfLastWord(string s) {
        int ans = 0;
        int r = s.size() - 1;
        while(r >= 0)
        {
            if(s[r] != ' ')
            ans++;
            else if(ans>0)
            return ans;
            r--;
        }
        return ans;
    }
};