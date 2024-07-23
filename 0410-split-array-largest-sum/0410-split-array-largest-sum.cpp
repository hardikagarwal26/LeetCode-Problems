class Solution {
public:
    int func(vector<int>& arr, int k){
    int painter=1;
    long long pagestud=0;
    for(int i=0;i<arr.size();i++){
        if(pagestud+arr[i]<=k){
            pagestud+=arr[i];
        }
        else{
            painter++;
            pagestud=arr[i];
        }
    }
    return painter;
}
    int splitArray(vector<int>& nums, int k) {
        int n=nums.size();
        if(k>n) return -1;
        int low=*max_element(nums.begin(),nums.end());
        int high=accumulate(nums.begin(),nums.end(),0);
        while(low<=high){
            int mid=(low+high)/2;
            int nop=func(nums,mid);
            if(nop>k)   low=mid+1;
            else high=mid-1;
        }
        return low;
    }
};