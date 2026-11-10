class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        result=0
        window=""
        for i in s:
            window=window[window.find(i)+1:]+i
            result=max(result,len(window))
        return result

