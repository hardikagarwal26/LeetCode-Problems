class Solution {
public:
    int maxele(vector<int>& nums){
        int maxi=INT_MIN;
        int n=nums.size();
        for(int i=0;i<n;i++){
            maxi=max(maxi,nums[i]);
        }
        return maxi;
    }
    int sumdiv(vector<int>& nums, int n){
        long long sum=0;
        for(int i=0;i<nums.size();i++){
            sum += ceil((double)(nums[i]) / (double)(n));
        }
        return sum;
    }
    int smallestDivisor(vector<int>& nums, int threshold) {
        int low=1,high=maxele(nums);
        while(low<=high){
            long long mid=high + (low - high) / 2;
            if(sumdiv(nums,mid)<=threshold)   high=mid-1;
            else low=mid+1;
        }
        return low;
    }
};