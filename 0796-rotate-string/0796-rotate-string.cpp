class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s.length()!=goal.length())   return false;
        for(int i=0;i<s.length();i++){
            string sub=s.substr(i)+s.substr(0,i);
            if(sub==goal)   return true;
        }
        return false;
    }
};