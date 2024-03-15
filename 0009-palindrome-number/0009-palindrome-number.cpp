class Solution 
{
public:
    bool isPalindrome(int x) 
    {
        int temp=x;
        if(x<0)
            return false;
        long revn=0;
        while(temp!=0)
        {
            int d= temp%10;
            revn = revn *10 + d;
            temp = temp/10;
        }
        if(revn==x)
            return true;
        return false;
    }
};