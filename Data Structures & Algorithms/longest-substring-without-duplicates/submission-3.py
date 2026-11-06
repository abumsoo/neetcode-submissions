class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        l, r = 0, 0
        length = 0

        while r < len(s):
            if s[r] in seen:
                length = max(length, r - l)
                while s[l] != s[r]:
                    del seen[s[l]]
                    l += 1
                l += 1
                r += 1
            else:
                seen[s[r]] = r
                r += 1

        return max(length, r - l)