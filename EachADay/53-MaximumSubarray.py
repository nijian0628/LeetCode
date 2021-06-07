class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        goahead = nums[0]
        currentrecord = nums[0]
        
        for i in range(1,len(nums)): # or x in nums[1:]:
            goahead = max(nums[i],goahead + nums[i]) # or max(x,goahead + x)
            currentrecord = max(goahead,currentrecord)        
        return currentrecord