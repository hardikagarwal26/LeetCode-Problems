class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> stck;
        for(int i=0;i<s.length();i++)
            if(s[i]=='(')
            stack.push(i);
            else if(s[i]==')')
            {
                if(stack.empty())
                s[i]='*';
                else
                stack.pop();
            }
        whiile(!stack.empty())
        s[stack.top()]='*',stack.pop();
        s.erase(remove(s.begin(),s.edn().'*'),s.end());
        return s;
    }
};