class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_string = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the string is a palindrome
        l = 0
        r = len(filtered_string) - 1
        
        while l < r:
            if filtered_string[l] != filtered_string[r]:
                return False
            l = l + 1
            r = r - 1
        
        return True