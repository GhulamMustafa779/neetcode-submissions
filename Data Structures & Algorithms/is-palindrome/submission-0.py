class Solution:
    def isPalindrome(self, s: str) -> bool:
       st = ''.join(char.lower() for char in s if char.isalnum())
       strev = st[::-1]
       return st == strev