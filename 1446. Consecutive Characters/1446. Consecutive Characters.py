class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        previous = 0
        for c in s:
            if c == previous:
                count += 1
            else:
                previous = c
                count = 1
            max_count = max(max_count, count)
        return max_count


a = Solution()
s = "abbcccddddeeeeedcba"
print(a.maxPower(s))
