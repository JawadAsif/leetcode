import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


s = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(s.majorityElement(nums))
