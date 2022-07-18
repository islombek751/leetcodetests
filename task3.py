#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s):  
        s = s[::-1]
        result = 0
        data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        def index_one():
            if len(s) > 1:
                if data[s[0]] > data[s[1]]:
                    return data[s[0]] - data[s[1]], True
                return data[s[0]], False
            return data[s], False
        while len(s) != 0:
            res = index_one()
            result += res[0]
            s = s[2:] if res[1] else s[1:]
        return result

e3 = Solution()
print(e3.romanToInt('MCMXCIV'))