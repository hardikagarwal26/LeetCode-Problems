class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n=nums.size();
        if(n==0)    return 0;
        int lng=1;
        unordered_set<int> st;
        for(int i=0;i<n;i++)
        {
            st.insert(nums[i]);
        }
        for(auto it:st)
        {
            if(st.find(it-1)==st.end())
            {
                int cnt=1;
                int x=it;
                while(st.find(x+1)!=st.end())
                {
                    x=x+1;
                    cnt=cnt+1;
                }
                lng=max(lng,cnt);
            }
        }
        return lng;
    }
};