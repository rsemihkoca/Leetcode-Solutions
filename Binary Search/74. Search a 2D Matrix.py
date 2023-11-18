class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        def binarySearch(nums, target):

            lo = 0

            hi = len(nums) - 1

            while lo <= hi:

                mid = (lo + hi) // 2

                if nums[mid] == target:
                    return True
                
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False
        

        lo = 0

        hi = len(matrix) - 1
    
        while lo <= hi:

            mid = (lo + hi) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binarySearch(matrix[mid], target)
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False