class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, end: int):
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1, end)                   # Recurse
                nums[start], nums[i] = nums[i], nums[start] 
        result = []
        backtrack(0, len(nums))
        return result