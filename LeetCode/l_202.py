#here we have to just see that while we are calculating the sumofSqures, we dont vist n which has been already visited, if it is , using hashSet we can determine it and return False

class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()

        while n not in visit:
            visit.add(n)
            n=self.sumOfSqaures(n)

            if n==1:
                return True
        
        return False
    
    def sumOfSqaures(self, n:int) -> int:
        output=0
        while n:
            digit=n%10
            digit=digit**2
            output+=digit
            n=n//10
        return output
        