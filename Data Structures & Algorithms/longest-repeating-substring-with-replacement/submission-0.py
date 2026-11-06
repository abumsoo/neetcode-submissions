class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        length = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_key = max(count, key=count.get)
            if r-l+1 - count[max_key] <= k:
                length = max(length, r-l+1)
            else:
                length = max(length, r-l-1)
                count[s[l]] -= 1
                l += 1
        return length