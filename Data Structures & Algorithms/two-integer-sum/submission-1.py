class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i,n in enumerate(nums):
            complement=target-n
            if complement in visited:
                return [visited[complement],i]
            visited[n]=i