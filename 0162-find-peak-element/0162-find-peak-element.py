class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start , end = 0 , len(nums)-1
        while start<=end:
            mid = start+((end-start)//2)
            if mid>0 and nums[mid] < nums[mid-1]:
                end = mid - 1
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                return mid

        