class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ind = 0
        count_rpt = 0
        count_diff = 0
        
        if len(nums) == 0:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] == val:
                    count_rpt = count_rpt+1
                else: # nums[i] != val
                    count_diff = count_diff+1
                    ind = count_diff-1
                    nums[ind] = nums[i]                    
        return count_diff