class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int c = 0;
        for(int i = 0 ; i< n; i++)
        {
            if(nums[c] != nums[i])
            {
                nums[c+1]=nums[i];
                c++;
            }
        }
        return c+1;
    }
};