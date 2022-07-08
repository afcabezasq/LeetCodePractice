class Solution:
    def isPalindrome(self, s: str) -> bool:
        A=''      
        for char in s:        
            if not char.isalnum():
                continue
            A += char.lower()           
        
        return A == A[::-1]