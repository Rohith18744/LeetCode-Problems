class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        resList=[]
        def recParenthesis(left,right,s,n):
            if len(s)==n*2:
                resList.append(s)
                return
            if left<n:
                recParenthesis(left+1,right,s+'(',n)
            if right<left:
                recParenthesis(left,right+1,s+')',n)
        recParenthesis(0,0,'',n)
        return resList