class Solution {
public:
    int climbStairs(int n) {
        int secondLast = 1;
        int last = 1;
        int sum = 0;
        for(int i=2;i<=n;i++) {
            sum = last + secondLast;
            secondLast = last;
            last = sum;
        }
        return last;
    }
};