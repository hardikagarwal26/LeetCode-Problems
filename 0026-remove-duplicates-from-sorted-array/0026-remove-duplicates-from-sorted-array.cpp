class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int c=0;
        int n= nums.size();
        for(int i = 0 ; i < n ; i++)
        {
            if(nums[i]!=nums[c])
            {
                nums[c+1]=nums[i];
                c++;
            }
        }
        return c+1;
    }
};