
from typing import List

# Bu soruda ilk defa neetcode çözümünün aynısını bakmadan yazdım.


# Ideal Solution, My Solution
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Yataydaki maks bulduktan sonra lo ve hi min değerden daha yüksege gelene kadar devam etsin.
        lo = 0

        hi = len(height) - 1

        max_area = 0

        curr_height = 0

        while lo < hi:

            length = hi-lo

            area = min(height[lo], height[hi]) * length

            max_area = max(max_area, area)

            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1


        
        return max_area






height = [1,8,6,2,5,4,8,3,7]
height = [1,2,3,4,5,25,24,3,4]



sol = Solution()
print(sol.maxArea(height))