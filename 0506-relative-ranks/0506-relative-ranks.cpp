class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<int> arr = score;
        sort(arr.begin(), arr.end(), greater<int>());
        int n = score.size();
        unordered_map<int, string> hash;
        for(int i=0; i<n; i++) {
            if(i==0) hash[arr[i]] = "Gold Medal";
            else if(i==1) hash[arr[i]] = "Silver Medal";
            else if(i==2) hash[arr[i]] = "Bronze Medal";
            else hash[arr[i]] = to_string(i+1);
        }
        vector<string> res;
        for(int i=0; i<n; i++) {
            res.push_back(hash.at(score[i]));
        }
        return res;
    }
};