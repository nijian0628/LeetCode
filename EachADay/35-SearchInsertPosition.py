class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i in range(len(nums)):
            if target == nums[i]: # target is in the list
                return i
            else: # target is not in the list
                if (i == 0) and (target < nums[i]): # smaller than head
                    return 0
                if (i == len(nums)-1) and (target > nums[i]): # greater than tail
                    return i+1
                if (target > nums[i]) and (target < nums[i+1]):
                    return i+1
            i = i+1