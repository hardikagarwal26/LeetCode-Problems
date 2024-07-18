class Solution {
public:
    int func(vector<int>& weights, int cap){
        int n=weights.size();
        int day=1,load=0;
        for(int i=0;i<n;i++){
            if(load+weights[i]>cap){
                day+=1;
                load=weights[i];
            }
            else load+=weights[i];
        }
        return day;
    }
    int shipWithinDays(vector<int>& weights, int days) {
        int low=*max_element(weights.begin(), weights.end());
        int high=accumulate(weights.begin(), weights.end(), 0);;
        while(low<=high){
            int mid=(low+high)/2;
            int ndays=func(weights,mid);
            if(ndays<=days) high=mid-1;
            else low=mid+1;
        }
        return low;
    }
};