from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, end: int):
            if start == end:
                result.append(nums[:])
            seen = set()
            for i in range(start, end):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1, end)                   # Recurse
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (swap back)

        nums.sort()  # Sort to make it easier to handle duplicates
        result = []
        backtrack(0, len(nums))
        return result

# Example usage:
sol = Solution()
data1 = [1, 1, 2]
permutations1 = sol.permuteUnique(data1)
print(permutations1)

data2 = [1, 2, 3]
permutations2 = sol.permuteUnique(data2)
print(permutations2)
