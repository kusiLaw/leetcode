class Solution(object):
    def firstPalindrome(self, words):
        for x in words:
            if(x == x[::-1]):
                return x
        return ""       