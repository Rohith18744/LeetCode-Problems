class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        previous = "1"
        
        for _ in range(2, n + 1):
            current = ""
            i = 0
            
            while i < len(previous):
                count = 1  
                while i + 1 < len(previous) and previous[i] == previous[i + 1]:
                    i += 1
                    count += 1
                
                
                current += str(count) + previous[i]
                i += 1  
            
            previous = current  
        
        return previous