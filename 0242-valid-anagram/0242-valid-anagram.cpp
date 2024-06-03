class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int>mp;
        unordered_map<char,int>mpp;
        for(auto i:s)
            mp[i]++;
        for(auto i:t)
            mpp[i]++;
        if(mp == mpp)
            return true;
        return false;
    }
};