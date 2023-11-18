"""
Notes
Counter are extends dictionaries

z = Counter()
z.update({1: 1}) increases the count of 1 by 1
z.update({1: -1}) decreases the count of 1 by 1

z += Counter() removes all elements with count <= 0 !!!!!


import collections
c = collections.Counter(a=-2, b=0, c=3)
c += collections.Counter()

print c
OUTPUT
Counter({'c': 3})


COUNTER OBJESI OLMAYAN KEYLER ICIN 0 DONER !!!!!

"""


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        eğer length olarak az isek r artmaya devam ta ki length eşit olana kadar
            eger r not in s1 ise left length sıfırla
        eğer anagram degilse left artsın
        """
        
        left = 0

        seen = Counter()

        s1_len = len(s1)
        
        s1_count = Counter(s1)

        for r in range(len(s2)):
            
            value = s2[r]

            if value not in s1:
                left = r + 1
                seen.clear()
                continue

            if (r - left + 1) < s1_len:
                seen.update({value: 1})
                continue
            elif (r - left + 1) == s1_len:
                seen.update({value: 1})
                
            if s1_count == seen:
                return True
            else:                
                seen.update({s2[left]: -1})
                left += 1

        return False



from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        eğer length olarak az isek r artmaya devam ta ki length eşit olana kadar
            eger r not in s1 ise left length sıfırla
        eğer anagram degilse left artsın
        """
        
        left = 0

        seen = Counter()

        s1_len = len(s1)
        
        s1_count = Counter(s1)

        for r in range(len(s2)):
            
            value = s2[r]

            # if value not in s1:
            #     left = r + 1
            #     seen.clear()
            #     continue

            if (r - left + 1) < s1_len:
                seen.update({value: 1})
                continue
            elif (r - left + 1) == s1_len:
                seen.update({value: 1})
                
            if s1_count == seen:
                return True
            else:                
                seen.update({s2[left]: -1})
                left += 1

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        eğer length olarak az isek r artmaya devam ta ki length eşit olana kadar
            eger r not in s1 ise left length sıfırla
        eğer anagram degilse left artsın
        """
        
        left = 0

        s1_len = len(s1)
        
        for r in range(len(s2)):
            
            value = s2[r]

            if value not in s1:
                left = r + 1
                continue
            
            if (r - left + 1) < s1_len:
                continue

            # HER SEFERINDE COUNTER OLUŞTURMAK YERINE MATCHES ADINDA BİR DEGİSKEN İLE BİLGİYİ TUTACAGIZ
            if Counter(s2[left: r+1]) == Counter(s1):
                return True
            else:
                left += 1

        return False



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        print("s1Count", s1Count,"\n", "s2Count", s2Count)
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left, matches, max_matches = 0, 0, 0

        s1_len = len(s1)

        s1_counter = Counter(s1)

        seen = Counter()
        
        for r in range(len(s2)):


            if s2[r] not in s1:
                seen.clear()
                matches = 0
                left = r
                continue

            seen.update({s2[r] : 1})

            if seen[s2[r]] == s1_counter[s2[r]]:
                matches += 1

            max_matches = max(max_matches, matches)

            if (r - left + 1) < s1_len:
                continue        

            if seen[s2[left]] == s1_counter[s2[left]] and seen[s2[left]] != 0:
                matches -= 1
            
            seen.update({s2[left] : -1})
            seen += Counter() # Removes keys <=0
            left += 1

        return max_matches == len(s1_counter)