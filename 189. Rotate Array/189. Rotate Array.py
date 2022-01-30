from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())


s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
s.rotate(nums, k)
print(nums)
