class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        digit_to_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []
        
       
        def backtrack(index, path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            possible_letters = digit_to_char[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return res


