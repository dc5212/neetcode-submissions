class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = ''.join(char.lower() for char in s if char.isalnum())
    
        l = 0
        r = len(filtered_string) - 1
        
        while l < r:
            if filtered_string[l] != filtered_string[r]:
                return False
            l = l + 1
            r = r - 1
        
        return True