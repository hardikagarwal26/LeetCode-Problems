class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       int n = nums.size();
        vector<int> left_products(n);
        vector<int> right_products(n);
        vector<int> answer(n);
        left_products[0] = 1;
        for (int i = 1; i < n; ++i) {
            left_products[i] = left_products[i - 1] * nums[i - 1];
        }
        right_products[n - 1] = 1;
        for (int i = n - 2; i >= 0; --i) {
            right_products[i] = right_products[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < n; ++i) {
            answer[i] = left_products[i] * right_products[i];
        }
        return answer; 
    }
};