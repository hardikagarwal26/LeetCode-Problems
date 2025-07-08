class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = (start +  end)//2
            if target == nums[mid]:
                return mid
            if nums[start] <= nums[mid]:
                if target > nums[mid] or target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            else : 
                if target > nums[end] or target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
        