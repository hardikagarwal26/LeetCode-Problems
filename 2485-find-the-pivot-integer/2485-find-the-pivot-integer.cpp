class Solution {
public:
    int pivotInteger(int n) {
        int sum = n*(n+1)/2;
        double ans = sqrt(sum);
        if(ans - ceil(ans) == 0)
            return int(ans);
        else
            return -1;
    }
};