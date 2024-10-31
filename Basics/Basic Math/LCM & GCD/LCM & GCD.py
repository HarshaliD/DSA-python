#https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1


class Solution:
    def lcmAndGcd(self, a , b):
        
        gcd_val = math.gcd(a,b)
        
        lcm_val = abs(a*b)//gcd_val
        
        return [lcm_val,gcd_val]

