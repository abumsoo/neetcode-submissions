class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        seen = { s[0] }

        l, r = 0, 1
        length = 1

        while r < len(s):
            if s[r] in seen:
                length = max(length, r - l)
                while s[l] != s[r]:
                    seen.discard(s[l])
                    l += 1
                l += 1
                r += 1
            else:
                seen.add(s[r])
                r += 1

        return max(length, r - l)