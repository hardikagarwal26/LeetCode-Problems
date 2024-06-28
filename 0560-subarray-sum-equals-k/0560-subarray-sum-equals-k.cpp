class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        map<int,int> mpp;
        mpp[0]=1;
        int prsm=0,cnt=0;
        for(int i=0;i<nums.size();i++)
        {
            prsm+=nums[i];
            int r=prsm-k;
            cnt+=mpp[r];
            mpp[prsm]+=1;
        }
        return cnt;
    }
};