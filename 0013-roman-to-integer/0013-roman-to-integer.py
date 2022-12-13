class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        l = len(s)
        for index in range(l):
            if index + 1 <  l and roman[s[index]] < roman[s[index + 1]]:
                    sum -= roman[s[index]]
            else:
                sum += roman[s[index]]
        return sum