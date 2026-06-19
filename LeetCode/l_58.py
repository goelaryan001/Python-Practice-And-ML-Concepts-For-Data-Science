#My solution is start from the end , dont count length of white spaces, and when u see a letter record length until u hit a space 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,length=len(s)-1,0
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!= " ":
            length+=1
            i-=1
        return length
        