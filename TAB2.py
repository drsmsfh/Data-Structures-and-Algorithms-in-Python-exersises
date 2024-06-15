class Solution(object):
    def isPalindrome(self, x):
        if x > -2^31 and x < 2^31 - 1:
            if x == 0:
                return True
            elif x < 0:
                return False
        def reverse_integer(x):
            reversed_int = 0
            while x!=0:
                reversed_int = reversed_int*10 + x%10
                x //=10
            return reversed_int
        if x == reverse_integer(x):
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome(121))