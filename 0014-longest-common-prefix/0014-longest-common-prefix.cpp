class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string s="";
        for(int i=0;i<strs[0].length();i++)
        {
            for(int j=1;j<strs.size();j++)
            {
                if(i>strs[j].length() || strs[j][i]!=strs[0][i])
                    return s;
            }
            s+=strs[0][i];
        }
        return s;
    }
};