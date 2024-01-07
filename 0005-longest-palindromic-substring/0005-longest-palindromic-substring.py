class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        cache = s[1]
        p1 = 0
        p2 = len(s) - 1
        switch = 0
        while p1 < len(s):
            sub = s[p1: p2 + 1]
            if sub == sub[::-1] and len(sub) > len(cache):
                    cache = sub
            if p1  >  p2 or len(sub) < len(cache) :
                p2 =  len(s) - 1
                p1 += 1
            else:
                p2 -= 1
             
        
        return cache
        