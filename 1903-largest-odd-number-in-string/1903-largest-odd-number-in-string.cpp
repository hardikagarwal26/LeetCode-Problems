class Solution {
public:
    string largestOddNumber(string num) {
        int n=num.size()-1;
        while(n>=0){
            if(num[n]%2==1) break;
            n--;
        }
        return num.substr(0,n+1);
    }
};