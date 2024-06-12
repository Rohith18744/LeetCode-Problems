class Solution:
    def canThreePartsEqualSum(self, arr):
        totalSum = sum(arr)
        if totalSum % 3 != 0:
            return False
        targetSum = totalSum // 3
        currentSum = 0
        partsFound = 0
        for num in arr:
            currentSum += num
            if currentSum == targetSum:
                currentSum = 0
                partsFound += 1
                if partsFound == 3:
                    return True
        
        return False