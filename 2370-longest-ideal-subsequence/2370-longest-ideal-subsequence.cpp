class Solution {
public:
    int longestIdealString(string s, int k) {
        vector<int> alpha(26,0);
        int ans=0;
        for(int i=0;i<s.size();i++)
        {
            int l=0;
            for(char ch = 'a' ; ch <= 'z'; ch++)
            {
                if(abs(s[i]-ch)<=k)
                {
                    l=max(l,alpha[ch-'a']+1);
                }
            }
            ans=max(ans,l);
            alpha[s[i]-'a']=l;
        }
        return ans;
    }
};