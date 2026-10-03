class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        dup = set()
        mx_count = 0

        for r in range(len(s)):
            if s[r] not in dup:
                dup.add(s[r])
            else:
                while s[r] in dup:
                    dup.remove(s[l])
                    l += 1
                dup.add(s[r])
            count = r - l + 1
            mx_count = max(mx_count, count)
        return mx_count