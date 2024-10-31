#https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1
        if(x<0):
            sign = -1
        else:
            sign = 1

        x = abs(x)
        
        reversed_num = int(str(x)[::-1])

        reversed_num*=sign

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0

        return reversed_num

#Time complexity = O(n)
#Space Complexity = O(n)
