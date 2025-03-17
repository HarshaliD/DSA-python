#Codility

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    
    maxNum = max(A)
    if(max<0):
        return 0

    for i in range(1,maxNum+1):
        if i not in A:
            return i

    #code should not reach here
    return -1
