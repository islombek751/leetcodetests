# #https://leetcode.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            reverse_x = ''
            for i in range(-1,-len(str(x))-1,-1):
                reverse_x += str(x)[i]
            if x == int(reverse_x):
                return True
            return False
                
e1 = Solution()
print(e1.isPalindrome(151))