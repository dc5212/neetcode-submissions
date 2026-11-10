class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        total=0
        for num in nums:
            if total<0:
                total=0
            total+=num
            res=max(total,res)
        return res