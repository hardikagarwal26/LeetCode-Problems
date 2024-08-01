class Solution {
public:
    // bool bs(vector<int>matrix , int target){
    //     int n=matrix.size();
    //     int low=0,high=n-1;
    //     while(low<=high){
    //         int mid=(low+high)/2;
    //         if(matrix[mid]==target){
    //             return true;
    //         }
    //         else if(matrix[mid]<mid)    high=mid-1;
    //         else low=mid+1;
    //     }
    //     return false;
    // }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n=matrix.size();
        int m=matrix[0].size();
        int low=0,high=(m*n-1);
        while(low<=high){
            int mid=(low+high)/2;
            int row=mid/m , col=mid%m;
            if(matrix[row][col]==target) return true;
            else if(matrix[row][col]<target) low=mid+1;
            else high=mid-1;
        }
        return false;
    }
};