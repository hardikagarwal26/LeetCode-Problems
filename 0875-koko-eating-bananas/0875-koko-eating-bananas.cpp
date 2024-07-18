class Solution {
public:
    int maxele(vector<int>& piles){
        int maxi=INT_MIN;
        int n=piles.size();
        for(int i=0;i<n;i++){
            maxi=max(maxi,piles[i]);
        }
        return maxi;
    }
    long long total(vector<int>& piles, int h) {
        long long tot=0;
        int n=piles.size();
        for(int i=0;i<n;i++){
            tot+=ceil((double)piles[i] / (double)h);
        }
        return tot;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int n=piles.size();
        int low=1,high=maxele(piles);
        while(low<=high){
            long long mid=(low+high)/2;
            int totalh=total(piles,mid);
            if(totalh<=h)    high=mid-1;
            else    low=mid+1;
        }
        return low;
    }
};