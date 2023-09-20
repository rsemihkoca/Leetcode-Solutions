from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]):

        if len(nums)==0:
            return 0

        sorted_nums = sorted(set(nums))
        sorted_nums += [sorted_nums[-1]+5]

        local_length = 1

        max_length = 1


        for index, value in enumerate(sorted_nums):
            if index!=len(sorted_nums)-1 :
                if self.isConsecutive(value, sorted_nums[index+1]):
                    local_length += 1
                    if local_length > max_length : 
                        max_length = local_length
                else:
                    local_length = 1

        return max_length




        
    def isConsecutive(self, a, b):

        return (b-a)==1

print(Solution().longestConsecutive([100,4,200,1,3,2]))