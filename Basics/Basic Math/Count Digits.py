#https://www.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides (self, N):
        n = len(str(N))
        count=0
        for i in range(n):
            num = (N//(10**i)%10)
            if(num!=0 and N%num==0):
                count+=1
        
        return count

