from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sol = [1] * length
        prefix, postfix = 1,1
        for key,value in enumerate(nums): #0 1 2 3 
            sol[key]*=prefix
            prefix*=value
            sol[-key-1]*=postfix
            postfix*=nums[-key-1]
        return(sol)

print(Solution().productExceptSelf([1,2,3,4]))
# prefix= 1 1 2 6
# postfix= 24 12 4 1    1 4 
# 4 3 2 1