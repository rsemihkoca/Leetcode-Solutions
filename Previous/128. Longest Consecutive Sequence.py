from typing import List

# Minimum çözüm

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

# Yeterli/Farklı çözüm

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

# İdeal çözüm

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0

        temp = sorted(list(set(nums)))
        
        i = 0
        j = 1

        count = 1
        curr = 1

        while j < len(temp):
            if temp[j] - 1 == temp[i]:

                curr += 1
                count = max(curr, count)

            else:
                curr = 1
            
            i = j
            j += 1

        return count


print(Solution().longestConsecutive([100,4,200,1,3,2]))