class Solution:
    def minWindow(self, s: str, t: str) -> str:

        """
        Runtime
Details
504ms
Beats 11.36%of users with Python3
Memory
Details
17.03MB
Beats 65.15%of users with Python3
"""
        ans=""
        occ = collections.Counter(t)
        track = dict()

        def test():
            for key, val in occ.items():
                if val >track[key]:
                    return False
            return True

        #init
        for k in occ.keys():
            track.update({k : 0})
        #first look
        left=0
        right=0
        for i in range(len(s)):
            if s[i] in occ.keys():
                left=i
                break
        
        for i in range(left,len(s)):
            
            #move right
            right=i
            if s[i] in occ.keys():
                track.update({s[i]:track[s[i]]+1})
                while test():
                    w=s[left:right+1]
                    if ans=="" or len(w)<len(ans):
                        ans=w
                    #move left
                    track.update({s[left]:track[s[left]]-1})

                    for j in range(left+1,right+1):
                        if s[j] in occ.keys():
                            left=j
                            break
        if (test()):
            if ans=="" or len(w)<len(ans):
                ans=w
        return ans
