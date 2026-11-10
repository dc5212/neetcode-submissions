class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        if not s:
            return 0
        count=0
        def expand(l,r):
            pc=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                pc=pc+1
                l-=1
                r+=1
            return pc
        for i in range(n):
            count+=expand(i,i)
            count+=expand(i,i+1)
        return count