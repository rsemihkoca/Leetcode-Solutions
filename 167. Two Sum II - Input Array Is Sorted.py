
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




        





class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        Runtime        5230 ms        Beats        5.3%
        Memory        17.2 MB        Beats        52.59%
        """
               
        for key, value in enumerate(numbers):

            complement = target - value
            pass_cache = set()

            if value in pass_cache:
                continue

            if complement in numbers:
                s = numbers.index(complement,key+1)
                return [key+1, s+1]
            else:
                pass_cache.add(value)
                continue


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