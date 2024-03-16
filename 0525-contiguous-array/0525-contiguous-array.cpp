class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int,int> mp;
        int maxi=0;
        int sum = 0;
        mp[0]=-1;
        for(int i = 0 ; i < nums.size() ; i++)
        {
            if(nums[i]==1)
            sum = sum+1;
            else
            sum= sum -1;
            if(mp.find(sum) != mp.end())
            maxi = max(maxi,i-mp[sum]);
            else
            mp[sum]= i;
        }
        return maxi;
    }
};