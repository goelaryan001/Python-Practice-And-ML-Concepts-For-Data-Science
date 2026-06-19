#Brute force: for starting letter b check every substring to see if it is a palindrome and repeat this for every character, now to check if it is a palindorme it will take O(N) number of substring is n^2:O(N^3)
#For every character, consider it as the center of a palindrome.
# Then expand outward and check how far the palindrome extends.
# We have N possible centers, and for each center we may expand up to N characters.
# Also need to handle both odd length palindromes ("aba") and even length palindromes ("abba").

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resLen=0

        for i in range(len(s)):
            #odd length
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)> resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1

            #even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)> resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                l-=1
                r+=1
        return res
        