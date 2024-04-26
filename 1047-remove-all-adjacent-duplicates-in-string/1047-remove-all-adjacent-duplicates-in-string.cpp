class Solution {
public:
    string removeDuplicates(string s) {
        stack<char> ans;
        for(int i=0;i<s.size();i++)
        {
            char ch=s[i];
            if(ans.empty())
            ans.push(ch);
            else if(ans.top()==ch)
            ans.pop();
            else
            ans.push(ch);

        }
        string st;
        while(!ans.empty())
        {
            st=ans.top()+st;
            ans.pop();
        }
        return st;
    }
};