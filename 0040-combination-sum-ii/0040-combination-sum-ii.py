from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self._find_combinations(candidates, target, 0, [], result)
        return result
    
    def _find_combinations(self, candidates, target, index, path, result):
        if target == 0:
            result.append(path)
            return
        if target < 0:
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self._find_combinations(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)
