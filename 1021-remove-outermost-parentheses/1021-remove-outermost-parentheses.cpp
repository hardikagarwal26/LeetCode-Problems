class Solution {
public:
    string removeOuterParentheses(string s) {
        int cnt=0;
        string ans="";
        for(int i=0;i<s.length();i++){
            if(s[i]=='(' && cnt==0)   cnt++;
            else if(s[i]=='(' && cnt>=1){
                ans+=s[i];
                cnt++;
            }
            else if(s[i]==')' && cnt>1){
                ans+=s[i];
                cnt--;
            }
            else if(s[i]==')' && cnt==1)   cnt--;
        }
        return ans;
    }
};