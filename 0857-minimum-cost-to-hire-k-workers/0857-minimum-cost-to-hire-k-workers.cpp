class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        vector<pair<double,int>> wqRatio;

        int n=quality.size();
        for(int i=0;i<n;i++){
            double Ration = static_cast<double>(wage[i]) / quality[i];
            wqRatio.push_back({Ration,quality[i]});
        }

        sort(wqRatio.begin(),wqRatio.end());

        priority_queue<int> pq;

        double ans=numeric_limits<double>::max();
        int currentQuality=0;

        for(int i=0;i<n;i++){
            currentQuality += wqRatio[i].second;
            pq.push(wqRatio[i].second);

            if(pq.size()>k){
                currentQuality-=pq.top();
                pq.pop();
            }

            if(pq.size()==k){
                ans=min(ans,currentQuality*wqRatio[i].first);
            }
        }

        return ans;
    }
};
