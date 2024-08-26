from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        
        if not s or not words:
            return []
        
        
        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        
        
        word_count = Counter(words)
        
       
        result = []
        
       
        for i in range(len(s) - total_length + 1):
            
            substring = s[i:i + total_length]
            
           
            seen_words = [
                substring[j:j + word_length] for j in range(0, total_length, word_length)
            ]
            
            
            if Counter(seen_words) == word_count:
                result.append(i)
        
        return result
