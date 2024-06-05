class Solution {
public:
    int reverse(int x) {
        long d=0,r=0;
        while(x!=0)
        {
            d = x%10;
            r = r*10 + d;
            x=x/10;
        }
        if(r<INT_MIN || r>INT_MAX)
        return 0;
        return r;
    }
};