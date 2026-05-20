class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "aab"
        max_length = 0
        letters_seen = set()
        left = 0
        
        for right in range(len(s)):
            if s[right] not in letters_seen:
                letters_seen.add(s[right])
                if len(letters_seen) > max_length:
                    max_length = len(letters_seen)
            else:
                while s[right] in letters_seen:
                    letters_seen.remove(s[left])
                    left += 1
                # letters_seen.remove(s[right])
            letters_seen.add(s[right])
            print(max_length)
            print(letters_seen)
        return max_length
