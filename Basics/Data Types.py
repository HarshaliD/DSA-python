#https://www.geeksforgeeks.org/problems/data-type-1666706751/1


class Solution:
    def dataTypeSize(self, str):
        if(str=="Character"):
            return 1
        elif(str=="Integer"):
            return 4
        elif(str=="Long"):
            return 8
        elif(str=="Float"):
            return 4
        elif(str=="Double"):
            return 8


'''
Time Complexity: 𝑂(1)
Space Complexity: O(1) (constant space)
'''
