class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = "".join(char for char in s if char.isalnum())
        reverse = "".join(s[i] for i in range(len(s) - 1, -1, -1))
        if s == reverse:
            return True
        else:
            return False