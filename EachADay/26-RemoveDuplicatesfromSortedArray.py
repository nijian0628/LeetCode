class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ind = 0
        count_rpt = 0
        count_diff = 1
        
        if len(nums) == 0:
            return 0
        else:
            tmp_val = nums[0]
            for i in range(1,len(nums)):
                if nums[i] == tmp_val:
                    count_rpt = count_rpt+1
                else: # nums[i] != tmp_val
                    count_diff = count_diff+1
                    tmp_val = nums[i]
                    ind = count_diff-1
                    nums[ind] = tmp_val                    
        return count_diff