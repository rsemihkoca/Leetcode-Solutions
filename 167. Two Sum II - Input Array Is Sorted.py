
from typing import List
import time

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:

#         for xkey, xvalue in enumerate(numbers):
#             for ykey, yvalue in enumerate(numbers):
#                 if xkey == ykey:
#                     continue
#                 if (xvalue+yvalue) == target:
#                     return [xkey+1, ykey+1]
# Time Limit Exceeded    

# Hash Table
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        val_counts = dict()


        for key, value in enumerate(numbers):

            compl = target - value
            
            if compl in val_counts:
                return [val_counts[compl]+1, key+1]

            else:
                val_counts[value] = key


# Two Pointers
class Solution:
    """
    Runtime    188 ms    Beats    5.36%
    Memory    17.2 MB    Beats    85.26%
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        
        lo = 0

        hi = len(numbers) - 1

        while lo <= hi:
            summed_value = numbers[lo] + numbers[hi]

            if summed_value == target:
                return [lo+1, hi+1]

            elif summed_value < target:
                lo += 1

            elif summed_value > target:
                hi -=1
        
        return False