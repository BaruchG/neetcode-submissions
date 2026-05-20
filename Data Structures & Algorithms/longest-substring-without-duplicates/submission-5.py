class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        string  = []
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[j] not in string:
                    string.append(s[j])
                    if len(string) > max_length:
                        max_length = len(string)
                else:
                    string = []
                    break
            string = []
        return max_length
                