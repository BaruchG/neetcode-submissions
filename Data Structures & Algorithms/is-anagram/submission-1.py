class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashsetS = {}
        hashsetT = {}

        for letter in s:
            if letter in hashsetS.keys():
                hashsetS[letter] += 1
            else:
                hashsetS[letter] = 1
        for letter in t:
            if letter in hashsetT.keys():
                hashsetT[letter] += 1
            else:
                hashsetT[letter] = 1
        if hashsetS == hashsetT:
            return True
        else:
            return False


        