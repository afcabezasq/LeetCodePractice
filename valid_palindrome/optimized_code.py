class Solution:
    def isPalindrome(self, s: str) -> bool:
        b, f = 0, len(s)-1
        s = s.lower()
        
        while b < f:            
            if not s[b].isalnum():
                b +=1
                continue
            if not s[f].isalnum():
                f -=1
                continue
            if s[f] != s[b]:
                return False
            b,f = b+1, f-1
        
        return True
            
            
    
    def alphaNum(self, c:str)->bool:
        return  (ord('A')<= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))