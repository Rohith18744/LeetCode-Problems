class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        resList=[]
        high,low=len(s),0
        k=1
        for ch in s:
            if ch=='i' or ch=='I':
                resList.insert(k,low)
                k+=1
                low+=1
            elif ch=='d' or ch=='D':
                resList.insert(k,high)
                k+=1
                high-=1
        resList.append(high)
        return resList