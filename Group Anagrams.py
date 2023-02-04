class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sup_list = []
        sub_list = []

        for i in strs:
            strs = strs.remove(i)
            sub_list.append(i)
            for z in strs:
                if isanagram(i, z):
                    sub_list.append(z)
                    strs.remove(z)
            sup_list.append[sub_list]
        return sup_list

    def isanagram(s, t):
        return Counter(s)== Counter(t)

print(Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))