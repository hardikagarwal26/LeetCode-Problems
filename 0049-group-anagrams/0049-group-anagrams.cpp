class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>mp;
        vector<vector<string>>ans;
        for(auto i:strs)
        {
            string wrd = i;
            sort(wrd.begin(),wrd.end());
            mp[wrd].push_back(i);
        }
        for(auto j:mp)
        {
            ans.push_back(j.second);
        }
        return ans;
    }
};