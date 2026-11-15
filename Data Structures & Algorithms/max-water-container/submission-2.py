class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        l=0
        r=len(heights)-1
        while l<r:
            currarea=min(heights[l],heights[r])*(r-l)
            area=max(area,currarea)
            if heights[l]<heights[r]:
                l=l+1
            else:
                r=r-1
        return area