class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        if len(s)==len(t):
            for i in s:
                if i in count:
                    count[i]+=1
                else:
                    count[i]=1
        print(count)
        for i in t:
            if i in count:
                count[i]-=1
            else:
                return False

        for i in count:
            if count[i] != 0:
                return False

        return True
        