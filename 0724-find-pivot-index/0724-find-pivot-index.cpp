class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n= nums.size();
        int s=0;
        for(int i=0;i<n;i++)
        {
            s+=nums[i];
        }
        int lefts=0;
        int rights=0;
        for(int i=0;i<n;i++){
            rights=s-lefts-nums[i];
            if(rights==lefts){
                return i;
            }
            lefts+=nums[i];
        }
        return -1;        
    }
};