class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in range(len(s)):
            if s[i].isalnum():
                st += s[i].lower()

        r = len(st) - 1
        l = 0

        while l < r:
            if st[l] != st[r]:
                return False
            else:
                l+=1
                r-=1
        
        return True