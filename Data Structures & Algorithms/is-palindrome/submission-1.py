class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        rev=s[::-1]
        print(rev)
        if rev == s:
            return True
        else:
            return False