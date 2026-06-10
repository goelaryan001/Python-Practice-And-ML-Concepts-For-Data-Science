class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        res = ""
        for r in range(numRows):
            increment= 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r>0 and r<numRows-1 and i+increment-2*r<len(s)):
                    res+=s[i+increment-2*r]




class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        i=0
        d=1
        rows=[[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i==0:
                d=1
            elif i==numRows-1:
                d=-1
            i += d

        res=''
        for i in range(numRows):
            res+=''.join(rows[i])

        return res    
            
        