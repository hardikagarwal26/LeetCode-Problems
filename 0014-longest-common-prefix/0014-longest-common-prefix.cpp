class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        int n=strs[0].size();
        string ans="";
        for(int i=0;i<n;i++){
            if(strs[0][i]==strs.back()[i])
                ans.push_back(strs[0][i]);
            else    break;
        }
        return ans;
    }
};