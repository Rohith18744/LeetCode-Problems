class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict={}
        for word in strs:
            wordSort=''.join(sorted(word))
            if wordSort not in resDict:
                resDict[wordSort]=[word]
            else:
                resDict[wordSort].append(word)
        return resDict.values()
        