class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)
        left,right=[0]*length,[0]*length
        trapped_water=0
        left[0]=height[0]
        right[-1]=height[-1]
        for i in range(1,length):
            left[i]=max(left[i-1],height[i])
        for i in range(length-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        for i in range(length):
            trapped_water+=min(left[i],right[i])-height[i]
        return trapped_water
        