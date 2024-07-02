class Solution:
        def validPalindrome(self, s: str) -> bool:
                def is_palindrome_range(s, l, r):
                    while l < r:
                        if s[l]!=s[r]:
                            return False
                        l+=1
                        r-=1
                    return True
                l,r=0,len(s)-1
                while l<r:
                    if s[l]==s[r]:
                        l+=1
                        r-=1
                    else:
                        return is_palindrome_range(s,l+1,r) or is_palindrome_range(s,l,r-1)
                return True
                      

                          
                                                                      






                                                                            

                                                                                       
                        
                          








        




    
      




   



   

        

    
 



  






  
        

        