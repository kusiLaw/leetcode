class Solution(object):
    def isHappy(self, n):
        repeat  = [] 
        
        while n not in repeat:
            repeat.append(n)
            n = self.sumOfSquares(n)
            print(n)
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self, n):
        return sum([int(x)**2 for x in str(n)])
        
         