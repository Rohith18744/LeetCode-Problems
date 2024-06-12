class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        from collections import Counter
        count = Counter(arr)
        occurrences = set(count.values())
        return len(occurrences) == len(count)