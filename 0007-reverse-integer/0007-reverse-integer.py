class Solution(object):
    def reverse(self, x):
        if self.constrain(x) == 0:
            return 0 
        return self.constrain(self.convert(x))

  
    def convert(self, x ):
        if x < 0:
            x = -1 * x
            x = int(str(x)[::-1])
            return -1 * x
        else:
            return int(str(x)[::-1])
        
    def constrain(self, x):
        if x < -2**31 :
            return 0
        if x > 2**31 :
            return 0
        return x
