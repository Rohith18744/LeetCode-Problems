class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=1
        n=len(colors)
        for i in range(n-1,-1,-1):
            if colors[i]!=colors[0]:
                temp=i
                ans=max(ans,temp)
                break
        for i in range(n):
            if colors[i]!=colors[n-1]:
                temp=n-1-i
                ans=max(ans,temp)
        return ans