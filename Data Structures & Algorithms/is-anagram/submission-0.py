class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        t1={}
        for i in s:
            if i in s1:
                s1[i]+=1
            else:
                s1[i]=1
        for j in t:
            if j in t1:
                t1[j]+=1
            else:
                t1[j]=1
        if s1==t1:
            return True
        else:
            return False