class Solution {
public:
    bool isValid(string s) {
        stack<int> a;
        for(int i = 0 ; i<s.size();i++)
        {
            if(s[i] == '(' || s[i] == '[' || s[i] == '{')
            a.push(s[i]);
            else
            {
                if(a.empty() == false)
                {
                    if(s[i] == ')' && a.top() == '(')
                    a.pop();
                    else if(s[i] == ']' && a.top() == '[')
                    a.pop();
                    else if(s[i] == '}' && a.top() == '{')
                    a.pop();
                    else
                    return false;
                }
                else
                return false;
            }
        }
        if(a.empty() == true)
        return true;
        return false;
    }
};