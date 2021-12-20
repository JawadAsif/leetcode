from typing import List
import sys


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr = sorted(arr)
        absMin = sys.maxsize
        # find absMin
        for i in range(1, len(arr)):
            m = arr[i]-arr[i-1]
            if m < absMin:
                absMin = m

        # find the pairs with absMin
        for i in range(1, len(arr)):
            m = arr[i]-arr[i-1]
            if m == absMin:
                res.append([arr[i-1], arr[i]])

        return res


s = Solution()
arr = [4, 2, 1, 3]
print(s.minimumAbsDifference(arr))
