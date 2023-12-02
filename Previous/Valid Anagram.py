class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

         # Top k frequent elements
         # [z[0] for z in Counter(nums).most_common(k)]