class Solution 
{
public:
    bool isPalindrome(int x) 
    {
        long temp=x;
        long ans=0;
        while(x!=0)
        {
            ans = ans*10 + x%10;
            x/=10;
        }
        if(temp == ans && temp>=0)
        return true;
        return false;
    }
};