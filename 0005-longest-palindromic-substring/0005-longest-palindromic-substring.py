class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        if len(s) == 0:
            return ""
        
        longest_palindrome = ""
        
        for i in range(len(s)):
           
            odd_palindrome = expandAroundCenter(i, i)
          
            even_palindrome = expandAroundCenter(i, i + 1)
            
            
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome
