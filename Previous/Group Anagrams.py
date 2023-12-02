from typing import List

class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = dict()
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in results.keys():
                results[sorted_string] = []

            results[sorted_string].append(string)
        return [*results.values()]

sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

#Sorting can help us group anagrams together.

#LOOP WHILE CHANGE LIST:
#or unify them into one loop via sort

# for item in a[:]:  # make a copy of the list
#     if even(item):
#         a.remove(item)
# # --> a = [1, 3]


# What NOT to do¶


# for item in a:
#     if even(item):
#         a.remove(item)
# # --> a = [1, 2, 3] !!!