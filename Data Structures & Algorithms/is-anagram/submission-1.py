class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_count={}
        for ch in s:
            character_count[ch]=character_count.get(ch,0)+1
        for ch in t:
            character_count[ch]=character_count.get(ch,0)-1
        for value in character_count.values():
            if value!=0:
                return False
        return True
